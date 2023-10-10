from data.delegation import general_data
from src.api.app import QiwaApi
from src.ui.qiwa import qiwa
from utils.helpers import set_cookies_for_browser


def login_and_open_delegation_dashboard_page(personal_number: str, sequence_number: int | str):
    qiwa_api = QiwaApi.login_as_user(personal_number=personal_number).select_company(
        sequence_number=int(sequence_number)
    )
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_delegation_dashboard_page()
    set_cookies_for_browser(cookies)
    qiwa.delegation_dashboard_page.wait_delegation_dashboard_page_to_load().select_english_localization_on_delegation_dashboard()
    return qiwa_api


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
    qiwa.delegation_details_page.wait_delegation_details_page_to_load().select_english_localization_on_delegation_details()
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
    qiwa.delegation_details_page.wait_delegation_details_page_to_load().select_english_localization_on_delegation_details()
    return delegation_details


def formatted_phone_number(phone_number: str) -> str:
    return f"{phone_number[:4]} {phone_number[4:6]} {phone_number[6:9]} {phone_number[9:]}"


def get_partners_names_for_delegation_details(partner_list: list):
    partner_names = []
    for partner in partner_list:
        partner_names.append(partner["partnerName"])
    return partner_names


def get_partners_phone_numbers_for_delegation_details(partner_list: list):
    partners_numbers = []
    for partner in partner_list:
        partner_phone = partner["partnerPhoneNumber"]
        formatted_partner_phone_number = formatted_phone_number(partner_phone)
        partners_numbers.append(formatted_partner_phone_number)
    return partners_numbers


def get_partners_request_status_for_delegation_details(partner_list: list):
    partner_request_statuses = []
    for partner in partner_list:
        if partner["status"] == general_data.PENDING:
            expected_status = general_data.PENDING_REQUEST
        else:
            expected_status = partner["status"].capitalize()
        partner_request_statuses.append(expected_status)
    return partner_request_statuses
