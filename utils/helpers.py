from datetime import datetime
from typing import Union
from urllib import parse

from requests.cookies import RequestsCookieJar
from selene.support.shared import browser


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
