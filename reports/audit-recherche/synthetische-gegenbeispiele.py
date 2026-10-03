from math import sqrt

# Ausschliesslich erfundene Werte, keine ESS-Daten.
def score(values):
    observed = [v for v in values if v is not None]
    return sum(observed) / len(observed)

def cdf(reference, value):
    return sum(v <= value for v in reference) / len(reference)

complete = (0.5, 0.0)
missing = (0.5, None)
reference = [(v, 1.0) for v in (0.0, 0.25, 0.5, 0.75)]
full_norm = [score(x) for x in reference]
mask_norm = [score((x[0], None)) for x in reference]
print("Missing-Beispiel:", {"vollstaendiger_score": score(complete), "teil_score": score(missing), "teil_score_vollnorm": cdf(full_norm, score(missing)), "teil_score_maskennorm": cdf(mask_norm, score(missing))})

values = [(0.5, v) for v in (0.0, 0.5, 1.0)]
print("Dominanz-Beispiel:", {"voll_scores": [score(v) for v in values], "ohne_variables_item": [score((v[0],)) for v in values]})

print("Differenzunsicherheit mit gleichen marginalen SE:", {str(rho): sqrt(0.1**2 + 0.1**2 - 2*rho*0.1*0.1) for rho in (0.9, -0.9)})

cases = ((0.0, 0.25, 1.0), (0.0, None, 0.75), (0.5, 0.5, None))
res = [abs(score([None if v is None else 1-v for v in x])-(1-score(x))) for x in cases]
print("Spiegelung fuer feste Missing-Maske:", {"faelle": len(cases), "max_fehlbetrag": max(res)})
