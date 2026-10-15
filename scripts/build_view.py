# Usage: python3 build_view.py <dashboard.html> <db_dir> <out.html>
# Turns the live Claude dashboard into a standalone page: tender + run data embedded,
# go/no-go choices saved in the viewer's own browser (the Claude database is not reachable from GitHub).
import json, glob, os, sys
src, db, out = sys.argv[1:4]
def load(coll):
    rows = []
    for f in sorted(glob.glob(os.path.join(db, coll, '*.json'))):
        d = json.load(open(f)); d = d.get('data', d)
        rows.append({'id': os.path.splitext(os.path.basename(f))[0], **d})
    return rows
tenders, runs = load('tenders'), load('runs')
runs.sort(key=lambda r: r.get('runAt', ''), reverse=True)
data = json.dumps({'tenders': tenders, 'runs': runs[:60]}, ensure_ascii=False).replace('</', '<\\/')

html = open(src, encoding='utf-8').read()
start = html.index('(async()=>{\n  const db=await claude.use("db");')
end = html.index('})();', start) + len('})();')
static = '''(()=>{
  const SNAP=%s;
  let mine={};try{mine=JSON.parse(localStorage.getItem("ktw-decisions")||"{}")}catch(e){}
  state.rows=SNAP.tenders.map(r=>mine[r.id]!=null?{...r,decision:mine[r.id]}:r);
  state.runs=SNAP.runs;
  state.db={doc:p=>({update:async v=>{mine[p.split("/")[1]]=v.decision;try{localStorage.setItem("ktw-decisions",JSON.stringify(mine))}catch(e){}}})};
  const run=SNAP.runs[0];
  $("foot").textContent="Snapshot of the Claude dashboard"+(run?" as of the "+fmtHK(Date.parse(run.runAt))+" sweep":"")+". Go/no-go changes here are saved only in your own browser; the team's shared decisions live in the Claude dashboard. Closing dates are Hong Kong time. Always confirm details on the issuer's official notice before bidding.";
  renderAll();
})();''' % data
html = html[:start] + static + html[end:]
assert 'claude.use' not in html
open(out, 'w', encoding='utf-8').write(html)
print(len(tenders), 'tenders,', len(runs), 'runs ->', out)
