from decimal import ROUND_HALF_UP, Decimal
from typing import Union
from urllib import parse

from requests.cookies import RequestsCookieJar
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


def dround(amount: float, num: int = 2):
    quantize = f'.{"1".zfill(num)}'
    return Decimal(f"{amount}").quantize(Decimal(quantize), rounding=ROUND_HALF_UP)
