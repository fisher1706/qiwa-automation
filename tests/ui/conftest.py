from datetime import datetime

import allure
import allure_commons
import pytest
from allure_commons.types import AttachmentType, LinkType
from selene import support
from selene.support.shared import browser
from selenium import webdriver

import config
from data.constants import SupportedBrowser
from src.ui.pages.login_page import LoginPage


@pytest.fixture
def go_to_auth_page():  # TODO: Remove usage
    login_page = LoginPage()
    login_page.visit()
    login_page.wait_page_to_load()


@pytest.fixture(autouse=True)
def setup_driver():
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    browser_name = config.settings.browser_name
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "prefs", {"download.default_directory": config.settings.download_dir}
    )
    if not config.settings.remote_url:
        chrome_options.headless = config.settings.headless
        driver = webdriver.Chrome(options=chrome_options)
    else:
        if browser_name not in SupportedBrowser.version:
            raise NameError(f"Defined browser name '{browser_name}' is not supported")
        chrome_options.set_capability("browserName", browser_name)
        chrome_options.set_capability("browserVersion", SupportedBrowser.version[browser_name])
        chrome_options.set_capability(
            "acceptInsecureCerts", config.settings.remote_acceptInsecureCerts
        )
        chrome_options.set_capability(
            "selenoid:options",
            {
                "enableVNC": config.settings.remote_enableVNC,
                "enableVideo": config.settings.remote_enableVideo,
                "enableLog": config.settings.remote_enableLog,
                "screenResolution": config.settings.screen_resolution,
            },
        )
        driver = webdriver.Remote(config.settings.remote_url, options=chrome_options)
    if config.settings.maximize_window:
        driver.maximize_window()
    else:
        driver.set_window_size(
            width=config.settings.window_width,
            height=config.settings.window_height,
        )
    browser.config.hold_driver_at_exit = config.settings.hold_browser_open
    browser.config.driver = driver
    yield
    if not config.settings.hold_browser_open:
        browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome == "failed":
        timestamp = datetime.now()
        screenshot = browser.last_screenshot
        if screenshot:
            with open(screenshot, "rb") as file:
                img = file.read()
            allure.attach(img, name=f"{timestamp}.png", attachment_type=AttachmentType.PNG)
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def attach_video_record_link(setup_driver):
    if config.settings.remote_url and config.settings.remote_enableVideo:
        allure.dynamic.link(
            f"https://selenoid-ui.qiwa.tech/video/{browser.driver.session_id}.mp4",
            LinkType.LINK,
            "Video record",
        )
