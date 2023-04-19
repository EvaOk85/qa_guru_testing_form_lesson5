import pytest
from selene import  browser


@pytest.fixture
def size_browser_management():
    browser.config.base_url= 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 4.0

    yield
    browser.quit()