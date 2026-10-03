"""Synthetische Prüfung von Planvorschlägen, kein ESS-Import oder Messmodell."""
from fractions import Fraction


def weighted_tertiles(category_weights):
    """Inverse gewichtete CDF; gebundene Antwortkategorien bleiben zusammen."""
    weights = {}
    for category, weight in category_weights.items():
        if type(category) is not int or not 0 <= category <= 10:
            raise ValueError("Nur gültige synthetische LR-Kategorien 0–10")
        value = Fraction(str(weight))
        if value < 0:
            raise ValueError("Negative Gewichte sind unzulässig")
        if value:
            weights[category] = value
    total = sum(weights.values(), Fraction(0))
    if not total:
        return {"status": "BLOCKIERT", "reason": "Keine gültige Bezugsmenge"}
    cuts, cumulative = [], Fraction(0)
    for category in sorted(weights):
        cumulative += weights[category]
        while len(cuts) < 2 and cumulative >= total * Fraction(len(cuts) + 1, 3):
            cuts.append(category)
    groups = [[c for c in sorted(weights) if c <= cuts[0]],
              [c for c in sorted(weights) if cuts[0] < c <= cuts[1]],
              [c for c in sorted(weights) if c > cuts[1]]]
    if any(not group for group in groups):
        return {"status": "BLOCKIERT", "reason": "Keine drei besetzten Gruppen ohne Aufteilung von Bindungen",
                "cuts": cuts}
    return {"status": "BESTANDEN", "scope": "Synthetische Kategoriendefinition, keine Gruppenabnahme",
            "cuts": cuts, "groups": groups,
            "weightedShares": [str(sum((weights[c] for c in group), Fraction(0)) / total) for group in groups]}


def climate_routing(c30):
    """Original DE-Q S.26: Ursache und Anwendbarkeit der Folgefragen getrennt."""
    if type(c30) is not int or c30 not in {1, 2, 3, 4, 5, 55, 77, 88}:
        raise ValueError("Nicht in diesem Fragebogenvertrag bestätigter Code")
    if c30 == 55:
        return {"causeType": "Sonderantwort", "causeOrdinal": None, "followupsAsked": False,
                "followupStatus": "STRUKTURELL_NICHT_ANWENDBAR"}
    if c30 in {77, 88}:
        return {"causeType": "VERWEIGERT" if c30 == 77 else "WEISS_NICHT", "causeOrdinal": None,
                "followupsAsked": True, "followupStatus": "ANTWORTPRUEFUNG_OFFEN"}
    return {"causeType": "Ursachenzuschreibung", "causeOrdinal": c30, "followupsAsked": True,
            "followupStatus": "ANTWORTPRUEFUNG_OFFEN"}
