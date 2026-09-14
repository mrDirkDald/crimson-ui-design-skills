#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re, sys

def get_json_path(obj, path):
    cur = obj
    for part in path.split('.'):
        if isinstance(cur, list): cur = cur[int(part)]
        else: cur = cur[part]
    return cur

def run_check(root, c):
    typ = c['type']; rel = c.get('file',''); p = root/rel if rel else root
    try:
        if typ == 'file_exists':
            ok = p.exists(); obs = str(p.exists())
        elif typ in ('contains','not_contains','regex','regex_absent','count_min','count_max'):
            txt = p.read_text(encoding='utf-8')
            if typ == 'contains': ok = c['value'] in txt; obs = f"contains={ok}"
            elif typ == 'not_contains': ok = c['value'] not in txt; obs = f"absent={ok}"
            elif typ == 'regex': ok = re.search(c['pattern'], txt, re.M|re.S) is not None; obs = f"regex={ok}"
            elif typ == 'regex_absent': ok = re.search(c['pattern'], txt, re.M|re.S) is None; obs = f"regex_absent={ok}"
            else:
                n = txt.count(c['value']); bound = c['count']
                ok = n >= bound if typ == 'count_min' else n <= bound
                obs = f"count={n}, bound={bound}"
        elif typ == 'json_equals':
            obj = json.loads(p.read_text(encoding='utf-8'))
            actual = get_json_path(obj, c['path']); ok = actual == c['value']; obs = repr(actual)
        else:
            return False, f"unsupported check type {typ}"
    except Exception as e:
        return False, f"error: {e}"
    return ok, obs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('fixture')
    ap.add_argument('workspace')
    ap.add_argument('--out')
    args = ap.parse_args()
    fixture = Path(args.fixture); workspace = Path(args.workspace)
    spec = json.loads((fixture/'checks.json').read_text(encoding='utf-8'))
    results=[]; score=0; total=0
    for c in spec['checks']:
        ok, obs = run_check(workspace,c)
        w = c.get('weight',1); total += w
        if ok: score += w
        results.append({'id':c['id'],'pass':ok,'weight':w,'observation':obs,'description':c['description']})
    out={'fixture':spec['id'],'score':score,'total':total,'pass':score==total,'results':results}
    text=json.dumps(out,indent=2)
    print(text)
    if args.out: Path(args.out).write_text(text,encoding='utf-8')
    sys.exit(0 if out['pass'] else 1)
if __name__=='__main__': main()
