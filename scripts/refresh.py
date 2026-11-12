import random, re
from datetime import datetime, timezone
from pathlib import Path
root = Path(__file__).resolve().parent.parent
ts = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
files = sorted((root / 'infra-bench').glob('*.html'))
rotate = []
for i, f in enumerate(files):
    t = f.read_text(encoding='utf-8')
    o = t
    t = re.sub(r'"dateModified":"[^"]+"', '"dateModified":"' + ts + '"', t)
    t = re.sub(r'最后更新：[0-9T:\-]+Z', '最后更新：' + ts, t)
    if t != o:
        f.write_text(t, encoding='utf-8')
    if i % 4 == 0:
        rotate.append(f.name)
print('updated', len(files), 'rotate5', rotate[:5])
