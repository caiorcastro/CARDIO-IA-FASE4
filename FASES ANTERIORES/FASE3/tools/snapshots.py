from playwright.sync_api import sync_playwright
import time

DASH_URL = "http://127.0.0.1:1880/ui"
FLOW_URL = "http://127.0.0.1:1880/"


def try_dismiss_notifications(page):
    # Press ESC a few times to close potential modals
    for _ in range(3):
        page.keyboard.press("Escape")
        time.sleep(0.3)
    # Click common buttons
    for label in ["Close", "OK", "Ok", "Got it", "Dismiss", "Fechar", "Entendi"]:
        try:
            page.get_by_role("button", name=label).click(timeout=800)
        except Exception:
            pass
    # Hide notification containers via CSS (best-effort)
    css = """
    .red-ui-notification, .red-ui-notifications, .red-ui-notification-box,
    .red-ui-editor-dialog, .red-ui-editor-shade, .red-ui-editor .ui-dialog,
    .red-ui-panels .editor-shade, .red-ui-banner, .red-ui-popover { display:none !important }
    """
    try:
        page.add_style_tag(content=css)
    except Exception:
        pass


def capture():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1400, "height": 900})
        page = ctx.new_page()

        # Dashboard screenshot
        page.goto(DASH_URL, wait_until="load")
        time.sleep(2)
        page.screenshot(path="FASE3/reports/images/node_red_dashboard.png", full_page=True)
        print("Saved FASE3/reports/images/node_red_dashboard.png")

        # Editor screenshot without notifications overlay
        page.goto(FLOW_URL, wait_until="load")
        try:
            page.wait_for_selector("#red-ui-workspace", timeout=6000)
        except Exception:
            pass
        try_dismiss_notifications(page)
        time.sleep(1.2)
        page.screenshot(path="FASE3/reports/images/node_red_flow.png", full_page=True)
        print("Saved FASE3/reports/images/node_red_flow.png")

        browser.close()


if __name__ == "__main__":
    capture()
