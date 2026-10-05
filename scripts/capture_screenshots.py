"""Capture selected Calispot prototype screens with the project's Playwright venv."""

from pathlib import Path
import re

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
PROTOTYPE = ROOT / "prototype" / "calispot-standalone.html"
OUTPUT = ROOT / "screenshots"

# (flow number, flow label, output name, optional in-screen tab to open)
SCREENS = [
    ("01", "ONBOARDING", "onboarding", None),
    ("05", "MAPA", "map", None),
    ("07", "SPOT DETAIL", "spot-detail", None),
    ("09", "REGISTRO SESIÓN", "session-log", None),
    ("04", "FEED", "feed", None),
    ("10", "QUESTS", "quests", None),
    ("11", "PERFIL", "profile", "RADAR"),
]


def locate_phone(page) -> None:
    found = page.evaluate(
        """() => {
          const candidates = [...document.querySelectorAll('div')];
          const phone = candidates.find((element) => {
            const rect = element.getBoundingClientRect();
            return Math.abs(rect.width - 390) < 2 && Math.abs(rect.height - 844) < 2;
          });
          if (phone) phone.setAttribute('data-calispot-phone', 'true');
          return Boolean(phone);
        }"""
    )
    if not found:
        raise RuntimeError("Could not locate the 390 x 844 phone mockup")


def main() -> None:
    if not PROTOTYPE.is_file():
        raise SystemExit(f"Prototype not found: {PROTOTYPE}")

    OUTPUT.mkdir(exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(
            viewport={"width": 1440, "height": 1100},
            device_scale_factor=2,
        )
        page.goto(PROTOTYPE.as_uri(), wait_until="domcontentloaded")
        page.wait_for_timeout(1800)

        for number, label, filename, tab in SCREENS:
            button_name = re.compile(rf"\b{number}\s+{re.escape(label)}\b", re.IGNORECASE)
            try:
                page.get_by_role("button", name=button_name).click(timeout=5000)
            except PlaywrightTimeoutError as error:
                raise RuntimeError(f"Could not select prototype flow: {label}") from error

            page.wait_for_timeout(450)
            locate_phone(page)

            if tab:
                try:
                    page.locator("[data-calispot-phone='true']").get_by_role(
                        "button", name=tab, exact=True
                    ).first.click(timeout=5000)
                    page.wait_for_timeout(450)
                except PlaywrightTimeoutError as error:
                    raise RuntimeError(f"Could not open tab '{tab}' on {label}") from error

            destination = OUTPUT / f"{filename}.png"
            page.locator("[data-calispot-phone='true']").screenshot(path=str(destination))
            print(f"Captured {destination.relative_to(ROOT)}")

        browser.close()


if __name__ == "__main__":
    main()
