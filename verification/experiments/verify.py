#!/usr/bin/env python3
"""Scoped offline replay; preserve assertions and original expected values."""
from collections import Counter, defaultdict
from pathlib import Path
import hashlib, json, sys
ROOT=Path(__file__).resolve().parent
if sys.flags.optimize:
    raise SystemExit("Run normal Python; assertion checks must remain enabled.")

def load(topic, name):
    return json.loads((ROOT / topic / name).read_text(encoding='utf-8'))

def check_louis():
    data = load('louis-xiii-june-1635', 'partial_predictions.json')
    totals = []
    for row in data['trials']:
        predicted = [row['mapping'].get(token) for token in row['tokens']]
        assert predicted == row['expected_predictions']
        count = sum(value is not None for value in predicted)
        assert (count, len(predicted)) == (row['mapped'], row['total'])
        totals.append([count, len(predicted)])
    assert totals == [[6, 18], [10, 21]]
    return {'status': 'passed', 'partial_coverage': totals,
            'scope': 'Frozen coverage, not plaintext accuracy or global blindness'}

if __name__ == "__main__":
    print(json.dumps({'louis-xiii-june-1635': check_louis()}, ensure_ascii=False, indent=2))
