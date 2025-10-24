from playwright.sync_api import sync_playwright
import time, os

WOKWI_URL = "https://wokwi.com/projects/445645684122269697"
NODERED_URLS = [
    ("http://127.0.0.1:1880/ui", "dashboard"),
    ("http://127.0.0.1:1880/", "editor"),
]

out_dir = os.path.join("assets", "videos")
os.makedirs(out_dir, exist_ok=True)

with sync_playwright() as p:
    # Record Node-RED UI
    for url, tag in NODERED_URLS:
        ctx = p.chromium.launch().new_context(record_video_dir=out_dir)
        page = ctx.new_page()
        page.goto(url, wait_until="load")
        time.sleep(4)
        page.mouse.move(400, 300)
        page.mouse.wheel(0, -200)
        time.sleep(2)
        page.close()
        ctx.close()
    
    # Record Wokwi
    ctx = p.chromium.launch().new_context(record_video_dir=out_dir)
    page = ctx.new_page()
    page.goto(WOKWI_URL, wait_until="load")
    # Try to start
    for name in ["Start the simulation", "Start", "Run"]:
        try:
            page.get_by_role("button", name=name).click(timeout=2000)
            break
        except Exception:
            pass
    time.sleep(8)
    page.close()
    ctx.close()

print("VIDEOS:")
for f in os.listdir(out_dir):
    if f.endswith(".webm"):
        print(os.path.join(out_dir, f))
