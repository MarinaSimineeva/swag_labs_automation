import pytest
from playwright.sync_api import sync_playwright
from data.config import Config


@pytest.fixture(scope='class')
def browser(request):
    playwright = sync_playwright().start()

    match Config.BROWSER:
        case 'firefox':
            browser = playwright.firefox.launch(
                headless=Config.HEADLESS
            )
        case 'chrome':
            browser = playwright.chromium.launch(
                headless=Config.HEADLESS
            )
        case _:
            raise ValueError(
                f'Please, specify desired browser type. Options: chrome, firefox. Actual: {Config.BROWSER}')

    context = browser.new_context(no_viewport=True)
    page_data = context.new_page()
    yield page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()
