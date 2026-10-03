"""Small strict validator for the fixed A-publication JSON Schema subset.

No dependencies, global field vocabulary or inference from arbitrary payloads.
The checked schema declares every path, R-status branch and array dimension.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import re

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "data/a-aggregate-public.schema.json"


def _require(condition):
    if not condition:
        raise ValueError("A_AGGREGATE_SCHEMA")


def _same(left, right):
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(_same(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(_same(a, b) for a, b in zip(left, right, strict=True))
    return left == right


def _check(value, rule, document):
    if "$ref" in rule:
        prefix = "#/$defs/"
        _require(rule["$ref"].startswith(prefix))
        return _check(value, document["$defs"][rule["$ref"][len(prefix):]], document)
    if "oneOf" in rule:
        successes = 0
        for branch in rule["oneOf"]:
            try:
                _check(value, branch, document)
                successes += 1
            except ValueError:
                pass
        _require(successes == 1)
        return
    kind = rule.get("type")
    valid_type = {"object": isinstance(value, dict), "array": isinstance(value, list),
                  "string": isinstance(value, str), "boolean": isinstance(value, bool),
                  "null": value is None,
                  "integer": isinstance(value, int) and not isinstance(value, bool),
                  "number": isinstance(value, (int, float)) and not isinstance(value, bool)}
    _require(kind in valid_type and valid_type[kind])
    if kind in ("number", "integer"):
        _require(math.isfinite(value))
    if "const" in rule:
        # JSON Schema numbers admit integer/real equivalents, never booleans.
        constant = rule["const"]
        _require(value == constant if kind in ("number", "integer") else _same(value, constant))
    if "enum" in rule:
        _require(any(_same(value, candidate) for candidate in rule["enum"]))
    if kind == "object":
        properties = rule["properties"]
        _require(set(rule["required"]).issubset(value) and
                 (rule.get("additionalProperties") is not False or set(value).issubset(properties)))
        for key, child in value.items():
            _require(key in properties)
            _check(child, properties[key], document)
    elif kind == "array":
        _require(rule.get("minItems", 0) <= len(value) <= rule.get("maxItems", len(value)))
        if rule.get("uniqueItems"):
            _require(all(not _same(a, b) for index, a in enumerate(value) for b in value[index + 1:]))
        for child in value:
            _check(child, rule["items"], document)
    elif kind == "string":
        _require(rule.get("minLength", 0) <= len(value) <= rule.get("maxLength", len(value)))
        if "pattern" in rule:
            _require(re.fullmatch(rule["pattern"], value) is not None)


def validate_a(value):
    schema = json.loads(SCHEMA_PATH.read_text())
    _check(value, schema, schema)
    return value
