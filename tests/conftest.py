import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture()
def web_browser():
    # driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    # browser.config.driver_options = driver_options
    browser.config.window_width = 1600
    browser.config.window_height = 1200
    browser.config.base_url = 'https://reqres.in'
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    driver = browser.open('/')

    yield driver

    # attach.add_html(browser)
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_video(browser)

    browser.quit()

