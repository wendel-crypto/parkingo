# Builds the WF-style case thumbnail (1200x900) used on Cases > App.
# Usage: python3 make_thumb.py out.webp "PLATE 13" "MOBILE APP · PARKING + UX" "Parkin'go" "PROTOTYPE" tint s1.png s2.png s3.png
import sys, pathlib, base64, asyncio
from playwright.async_api import async_playwright
out, plate, sub, title, pill, tint, *shots = sys.argv[1:]
F = pathlib.Path('/tmp/fonts/node_modules/@fontsource')
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
syne = b64(F/'syne/files/syne-latin-800-normal.woff2'); mono = b64(F/'jetbrains-mono/files/jetbrains-mono-latin-500-normal.woff2')
imgs = [f'data:image/png;base64,{b64(s)}' if s.endswith('.png') else f'data:image/jpeg;base64,{b64(s)}' for s in shots]
html = f'''<!doctype html><meta charset=utf-8><style>
@font-face{{font-family:S;src:url(data:font/woff2;base64,{syne});font-weight:800}}
@font-face{{font-family:M;src:url(data:font/woff2;base64,{mono});font-weight:500}}
*{{box-sizing:border-box;margin:0}}body{{width:1200px;height:900px;position:relative;overflow:hidden;background:#0b0b0c;font-family:M}}
.bg{{position:absolute;inset:0;background:radial-gradient(ellipse 70% 55% at 50% 100%,{tint},transparent 70%),radial-gradient(ellipse 60% 40% at 50% 45%,rgba(255,255,255,.035),transparent 70%)}}
.cr{{position:absolute;width:26px;height:26px}}.cr:before,.cr:after{{content:"";position:absolute;background:#555}}.cr:before{{left:12px;top:0;width:1px;height:26px}}.cr:after{{top:12px;left:0;height:1px;width:26px}}
.fr{{position:absolute;inset:30px;border:1px solid rgba(255,255,255,.06)}}
.h1{{position:absolute;left:72px;top:64px;font-size:18px;letter-spacing:.2em;color:#8b8b8b;white-space:pre}}
.h2{{position:absolute;right:72px;top:64px;font-size:18px;letter-spacing:.2em;color:#c7f23a}}
.ph{{position:absolute;width:250px;aspect-ratio:390/844;border-radius:40px;border:6px solid #1f1f22;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.55),0 0 0 1px #3a3a3e;background:#000}}.ph img{{width:100%;height:100%;display:block;object-fit:cover}}
.p0{{left:195px;top:150px;transform:rotate(-8deg)}}.p1{{left:475px;top:105px;z-index:2}}.p2{{left:755px;top:150px;transform:rotate(8deg)}}
.ln{{position:absolute;left:72px;right:72px;top:760px;height:1px;background:rgba(255,255,255,.12)}}
.t{{position:absolute;left:72px;top:{782 if len(title)<10 else 792}px;font-family:S;font-weight:800;font-size:{76 if len(title)<10 else 60}px;line-height:1;color:#f4f4f4;letter-spacing:-.01em}}
.pill{{position:absolute;right:72px;top:804px;height:36px;padding:0 20px;border:2px solid #c7f23a;border-radius:20px;color:#c7f23a;font-size:20px;letter-spacing:.14em;display:flex;align-items:center}}
</style><div class=bg></div><div class=fr></div>
<div class=cr style="left:20px;top:20px"></div><div class=cr style="right:20px;top:20px"></div><div class=cr style="left:20px;bottom:20px"></div><div class=cr style="right:20px;bottom:20px"></div>
<div class=h1>{plate}  —  {sub}</div><div class=h2>WF ▪ CASE STUDY</div>
<div class="ph p0"><img src="{imgs[0]}"></div><div class="ph p2"><img src="{imgs[2]}"></div><div class="ph p1"><img src="{imgs[1]}"></div>
<div class=ln></div><div class=t>{title}</div><div class=pill>{pill}</div>'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width':1200,'height':900})
        await pg.set_content(html); await pg.wait_for_timeout(800)
        await pg.screenshot(path='/tmp/_t.png'); await b.close()
asyncio.run(main())
from PIL import Image
im = Image.open('/tmp/_t.png').convert('RGB'); im.save(out, 'WEBP', quality=88, method=6); print('saved', out)
