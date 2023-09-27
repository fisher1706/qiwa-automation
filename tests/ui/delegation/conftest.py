from src.api.app import QiwaApi
from src.ui.qiwa import qiwa
from utils.helpers import set_cookies_for_browser


def login_and_open_delegation_details_page_by_status(
    personal_number: str, sequence_number: int | str, status: str
):
    qiwa_api = QiwaApi.login_as_user(personal_number=personal_number).select_company(
        sequence_number=int(sequence_number)
    )
    headers = qiwa_api.delegation_api.set_headers()
    delegation_list = qiwa_api.delegation_api.get_delegations_by_status(headers, status_en=status)
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_delegation_details_page(delegation_list.first_delegation_id)
    set_cookies_for_browser(cookies)
    return delegation_list


def login_and_open_delegation_details_page(personal_number: str, sequence_number: int | str):
    qiwa_api = QiwaApi.login_as_user(personal_number=personal_number).select_company(
        sequence_number=int(sequence_number)
    )
    headers = qiwa_api.delegation_api.set_headers()
    delegation_list = qiwa_api.delegation_api.get_delegations(headers)
    delegation_details = qiwa_api.delegation_api.get_delegation_by_id(
        headers, delegation_list.first_delegation_id
    )
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_delegation_details_page(delegation_list.first_delegation_id)
    set_cookies_for_browser(cookies)
    return delegation_details
