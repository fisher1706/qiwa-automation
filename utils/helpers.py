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
