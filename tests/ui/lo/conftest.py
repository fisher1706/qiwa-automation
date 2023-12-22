import pytest
from selene.support.shared import browser
from seleniumwire import webdriver as wire_webdriver

import config


@pytest.fixture
def inspected_driver_setup(setup_driver):
    driver = browser.config.driver
    capabilities = driver.capabilities

    options = wire_webdriver.ChromeOptions()
    # TODO: investigate why AttributeError: can't set attribute 'capabilities'
    # options.capabilities = capabilities
    inspected_driver = wire_webdriver.Chrome(options=options)

    if config.settings.remote_url:
        inspected_driver = wire_webdriver.Remote(config.settings.remote_url, options=options)

    browser.config.driver = inspected_driver

    yield

    browser.config.driver = driver
