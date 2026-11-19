# Renders screenshots of app/index.html with headless Chrome and reports console errors.
# Usage: python3 scripts/shoot.py [lang]   (writes to build/shots-<lang>/)
import asyncio, pathlib, sys
from playwright.async_api import async_playwright

root = pathlib.Path(__file__).resolve().parent.parent
APP = (root / 'app' / 'index.html').as_uri()
lang = sys.argv[1] if len(sys.argv) > 1 else 'en'
out = root / 'build' / ('shots-' + lang)
out.mkdir(parents=True, exist_ok=True)
SHOTS = [('01-intro','intro',''),('02-welcome','welcome',''),('03-options','options',''),('04-email','email',''),('05-plate','plate',''),('06-payment','pay',''),('07-vehicle-type','vtype',''),('08-vehicle','vehicle',''),
 ('09-explore','home',''),('10-search','search','&flt=cov'),('11-spot','spot','&spot=brk'),('12-bay','bay','&spot=brk'),('13-route','route','&spot=brk'),('14-directions','drive','&spot=brk'),('15-trip','trip','&spot=brk'),('16-arrival','arrive','&spot=brk'),
 ('17-checkin','checkin',''),('18-session','session',''),('19-extend','extend',''),('20-checkout','checkout',''),('21-activity','activity',''),('22-receipt','receipt','&rc=0'),('23-statistics','stats',''),('24-profile','profile','')]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=2)
        errs = []
        pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
        pg.on('pageerror', lambda e: errs.append(str(e)))
        for name, screen, extra in SHOTS:
            await pg.goto(f'{APP}?bare&lang={lang}&screen={screen}{extra}')
            await pg.wait_for_timeout(1500)
            await pg.screenshot(path=str(out / f'{name}.png'))
        await b.close()
        print('shots', len(SHOTS), 'errors', errs)

asyncio.run(main())
