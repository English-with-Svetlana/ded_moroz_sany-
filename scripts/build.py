"""Build an allowlisted Pages artifact; never copy source or obsolete media."""
from pathlib import Path
import hashlib
import re
import shutil

root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text()
matches = re.findall(r'src="(media/sleigh\.([a-f0-9]{16})\.mp4)"', html)
assert len(matches) == 1, 'Expected exactly one hashed video reference'
media, digest = matches[0]
source = root / media
assert source.is_file() and not source.is_symlink()
assert hashlib.sha256(source.read_bytes()).hexdigest().startswith(digest)
out = root / '_site'
if out.exists():
    shutil.rmtree(out)
(out / 'media').mkdir(parents=True)
for name in ('index.html', '.nojekyll', media):
    shutil.copyfile(root / name, out / name)
assert sorted(str(p.relative_to(out)) for p in out.rglob('*') if p.is_file()) == sorted(['index.html', '.nojekyll', media])
print('Validated artifact:', ', '.join(['index.html', '.nojekyll', media]))
