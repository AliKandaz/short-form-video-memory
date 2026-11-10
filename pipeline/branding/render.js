// Screenshot a local HTML file at an exact pixel size with the preinstalled Playwright Chromium.
//   node render.js page.html out.png 2560 1440 [full]
// "full" captures the whole page height instead of just the viewport. The page may set
// body[data-ready="1"] when its own layout script has finished (e.g. fitting the headline).
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const [html, out, w, h, full] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(html));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForSelector('body[data-ready="1"]', { timeout: 5000 }).catch(() => {});
  await page.waitForTimeout(200);
  await page.screenshot({ path: out, fullPage: full === 'full' });
  await browser.close();
  console.log('rendered', out);
})();
