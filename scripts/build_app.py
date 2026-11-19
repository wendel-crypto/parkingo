# Builds app/index.html from src/app.html: inlines the photos (as CSS variables) and the demo QR code
# so the app stays one self-contained file. Run from the repo root: python3 scripts/build_app.py
import base64, pathlib, segno

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'src' / 'app.html').read_text(encoding='utf-8')

photos = ':root{' + ''.join(
    f'--ph-{p.stem}:url(data:image/webp;base64,{base64.b64encode(p.read_bytes()).decode()});'
    for p in sorted((root / 'src' / 'photos').glob('*.webp'))) + '}'

# The QR opens the case study, so scanning the demo code never looks like a real transaction.
qr = segno.make('https://www.wendelfreitas.com/parkingo/?ref=demo', error='m')
rows = [list(r) for r in qr.matrix]
path = ''.join(f'M{x} {y}h1v1h-1z' for y, r in enumerate(rows) for x, v in enumerate(r) if v)

out = (src.replace('/*__PHOTOS__*/', photos)
          .replace('__QRN__', str(len(rows)))
          .replace('__QR__', path))
(root / 'app').mkdir(exist_ok=True)
(root / 'app' / 'index.html').write_text(out, encoding='utf-8')
print('app/index.html', len(out), 'bytes; QR', len(rows), 'modules')
