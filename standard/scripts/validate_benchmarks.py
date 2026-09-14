#!/usr/bin/env python3
from pathlib import Path
import json,sys
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
B=ROOT/'evaluation/benchmarks'; F=ROOT/'evaluation/fixtures'
errors=[]
try:
    schema=json.loads((ROOT/'evaluation/benchmark.schema.json').read_text(encoding='utf-8'))
    Draft202012Validator.check_schema(schema)
    validator=Draft202012Validator(schema)
except Exception as e:
    print('ERRORS:\n- invalid benchmark schema:',e); sys.exit(1)
specs=sorted(B.glob('*.json')); ids=set()
if len(specs)<13: errors.append(f'Expected >=13 benchmark specs, found {len(specs)}')
for p in specs:
    try:d=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{p.name}: invalid JSON {e}'); continue
    verr=sorted(validator.iter_errors(d), key=lambda e:list(e.path))
    for e in verr: errors.append(f"{p.name}: schema: {'/'.join(map(str,e.path)) or '<root>'}: {e.message}")
    bid=d.get('id'); ids.add(bid)
    if bid and not (F/bid).exists(): errors.append(f'{p.name}: executable fixture missing')
    if bid and (F/bid/'checks.json').exists():
        fx=json.loads((F/bid/'checks.json').read_text(encoding='utf-8'))
        spec_ids={x.get('id') for x in d.get('machine_checks',[])}
        fixture_ids={x.get('id') for x in fx.get('checks',[])}
        if spec_ids!=fixture_ids: errors.append(f'{p.name}: machine-check IDs do not match executable fixture')
fixture_ids={p.name for p in F.iterdir() if p.is_dir()} if F.exists() else set()
if ids!=fixture_ids: errors.append(f'Benchmark/fixture ID mismatch specs={sorted(ids)} fixtures={sorted(fixture_ids)}')
if errors:
    print('ERRORS:'); [print('-',e) for e in errors]; sys.exit(1)
print(f'OK: {len(specs)} benchmark specs pass JSON Schema and align with {len(fixture_ids)} executable fixtures.')
