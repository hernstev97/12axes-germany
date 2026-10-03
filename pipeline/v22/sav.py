"""Minimal reader for SPSS system files (.sav), standard library only.

Supports what the ESS5 country SDDF uses: little-endian files, numeric and short or
long string variables, uncompressed or bytecode-compressed data (compression 1).
Labels, documents and extension records are skipped. Returns raw values per variable:
float or None (system missing) for numeric, str (right-stripped) for string variables.
"""

from __future__ import annotations

import struct
import sys
from pathlib import Path


class SavError(ValueError):
    pass


def read_sav(path: Path, wanted: list[str]) -> list[dict[str, object]]:
    data = path.read_bytes()
    if data[:4] not in (b'$FL2', b'$FL3'):
        raise SavError('not an SPSS system file')
    layout = struct.unpack_from('<i', data, 64)[0]
    if layout not in (2, 3):
        raise SavError('unsupported byte order')
    compression = struct.unpack_from('<i', data, 72)[0]
    n_cases = struct.unpack_from('<i', data, 80)[0]
    bias = struct.unpack_from('<d', data, 84)[0]
    if compression not in (0, 1):
        raise SavError('unsupported compression')
    pos = 176
    variables: list[tuple[str, int, int]] = []  # name, width (0 numeric), segments
    while True:
        record = struct.unpack_from('<i', data, pos)[0]
        if record == 2:
            width, has_label, n_missing = struct.unpack_from('<iii', data, pos + 4)
            name = data[pos + 24:pos + 32].decode('latin1').strip().lower()
            pos += 32
            if has_label:
                length = struct.unpack_from('<i', data, pos)[0]
                pos += 4 + ((length + 3) // 4) * 4
            pos += 8 * abs(n_missing)
            if width == -1:
                continue  # continuation of a long string
            segments = 1 if width == 0 else (width + 7) // 8
            variables.append((name, width, segments))
        elif record == 3:
            count = struct.unpack_from('<i', data, pos + 4)[0]
            pos += 8
            for _ in range(count):
                label_length = data[pos + 8]
                pos += 8 + ((label_length + 1 + 7) // 8) * 8
        elif record == 4:
            count = struct.unpack_from('<i', data, pos + 4)[0]
            pos += 8 + 4 * count
        elif record == 6:
            lines = struct.unpack_from('<i', data, pos + 4)[0]
            pos += 8 + 80 * lines
        elif record == 7:
            size, count = struct.unpack_from('<ii', data, pos + 8)
            pos += 16 + size * count
        elif record == 999:
            pos += 8
            break
        else:
            raise SavError('unknown dictionary record')
    names = [name for name, _, _ in variables]
    missing = [name for name in wanted if name not in names]
    if missing:
        raise SavError(f'variables not in file: {missing}')
    slots = sum(segments for _, _, segments in variables)

    def cells():
        nonlocal pos
        if compression == 0:
            while pos + 8 <= len(data):
                yield data[pos:pos + 8]
                pos += 8
            return
        while pos + 8 <= len(data):
            codes = data[pos:pos + 8]
            pos += 8
            for code in codes:
                if code == 0:
                    continue
                if code == 252:
                    return
                if code == 253:
                    yield data[pos:pos + 8]
                    pos += 8
                elif code == 254:
                    yield b' ' * 8
                elif code == 255:
                    yield None
                else:
                    yield ('number', code - bias)

    stream = cells()
    rows = []
    for _ in range(n_cases):
        raw = [next(stream) for _ in range(slots)]
        row: dict[str, object] = {}
        index = 0
        for name, width, segments in variables:
            parts = raw[index:index + segments]
            index += segments
            if name not in wanted:
                continue
            if width == 0:
                cell = parts[0]
                if cell is None:
                    row[name] = None
                elif isinstance(cell, tuple):
                    row[name] = float(cell[1])
                else:
                    value = struct.unpack('<d', cell)[0]
                    row[name] = None if value == -sys.float_info.max else value
            else:
                text = b''.join(b' ' * 8 if p is None or isinstance(p, tuple) else p for p in parts)
                row[name] = text[:width].decode('latin1').rstrip()
        rows.append(row)
    return rows
