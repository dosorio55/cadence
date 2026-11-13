import json
from pathlib import Path
p=Path(__file__).parent/'pending-013'
c=p/'checks'
for name,prefix in [('stages','stage-independence-013'),('progressions','prog-independence-013'),('chord-events','chord-independence-013'),('note-events','note-independence-013')]:
    dst=c/f'{name}.json'
    existing=json.loads(dst.read_text())
    records=json.loads((p/f'{name}.json').read_text())
    existing.extend(row for row in records if row['id'].startswith(prefix))
    dst.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n')
