import time
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path
from time import sleep
from typing import Union
from urllib import parse

from requests import Response
from requests.cookies import RequestsCookieJar
from selene import Element, command
from selene.api import have
from selene.support.shared import browser

from data.visa.constants import ENV_VARIABLES
from utils.logger import yaml_logger

logger = yaml_logger.setup_logging(__name__)

GET_SESSION_VARS_JS = """var ls = window.sessionStorage, items = {};
                         for (var i = 0, k; i < ls.length; ++i)  
                         items[k = ls.key(i)] = ls.getItem(k);  
                         return items; """


def join_codes(code: str, times: int) -> str:
    return ", ".join([code] * times)


def set_cookies_for_browser(cookies: RequestsCookieJar):
    cookies = [
        {"name": "QIWA_SIGNED_IN", "value": cookies["QIWA_SIGNED_IN"], "domain": "qiwa.info"},
        {
            "name": "qiwa.authorization",
            "value": cookies["qiwa.authorization"],
            "domain": "qiwa.info",
        },
    ]
    for cookie in cookies:
        browser.driver.add_cookie(cookie)


def get_url_param(param_name: Union[str, None] = None) -> Union[str, None]:
    url = browser.driver.current_url
    parsed_url = parse.urlparse(url)
    params = parse.parse_qs(parsed_url.query)
    if param_name:
        if param_name in params:
            return params[param_name][0]
    else:
        return parsed_url.path[1:]
    return None


def get_session_variable(variable):
    session_variables = browser.config.driver.execute_script(GET_SESSION_VARS_JS)
    try:
        env = session_variables[variable] == "true"
    except KeyError:
        env = None
        logger.warning(
            f"Environment variable '{variable}' could not be found in session. Either typo or it "
            f"was removed by mistake. Thera are should be available variables: {ENV_VARIABLES}"
        )
    return env


def verify_new_tab_url_contains(url):
    browser.driver.switch_to.window(browser.driver.window_handles[-1])
    browser.should(have.url_containing(url))
    browser.driver.close()
    browser.driver.switch_to.window(browser.driver.window_handles[0])


def save_pdf_file_from_response(response: Response, file_name: str):
    file_path = Path(__file__).parent.parent.joinpath("data/files").joinpath(f"{file_name}.pdf")
    with open(file_path, "wb") as pdf_file:
        pdf_file.write(response.content)
    return file_path


def dround(amount: float, num: int = 2):
    quantize = f'.{"1".zfill(num)}'
    return Decimal(f"{amount}").quantize(Decimal(quantize), rounding=ROUND_HALF_UP)


def scroll_to_coordinates(x: str = "0", y: str = "0"):
    for _ in range(2):
        sleep(3)
        browser.driver.execute_script(f"window.scrollTo({x}, {y});")


def scroll_to_element_into_view(element: Element, timeout=0.5):
    element.perform(command.js.scroll_into_view)
    time.sleep(timeout)
