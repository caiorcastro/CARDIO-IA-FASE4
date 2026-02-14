from playwright.sync_api import sync_playwright
import time

URL = "https://wokwi.com/projects/445645684122269697"
OUT1 = "FASE3/reports/images/wokwi_running.png"
OUT2 = "FASE3/reports/images/esp32_flush_queue.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    ctx = browser.new_context(viewport={"width": 1400, "height": 900})
    page = ctx.new_page()
    page.goto(URL, wait_until="load")
    # Start simulation
    for name in ["Start the simulation", "Start", "Run"]:
        try:
            page.get_by_role("button", name=name).click(timeout=2000)
            break
        except Exception:
            pass
    time.sleep(8)
    page.screenshot(path=OUT1, full_page=True)
    # Wait extra time to allow offline window to end and flush to happen
    time.sleep(10)
    page.screenshot(path=OUT2, full_page=True)
    print("Saved", OUT1, OUT2)
    browser.close()
