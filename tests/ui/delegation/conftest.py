import random

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


def login_and_open_add_delegation_page(personal_number: str, sequence_number: int | str):
    qiwa_api = QiwaApi.login_as_user(personal_number=personal_number).select_company(
        sequence_number=int(sequence_number)
    )
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_add_new_delegation_page()
    set_cookies_for_browser(cookies)
    qiwa.add_delegation_page.wait_add_new_delegation_page_to_load().select_english_localization_on_add_delegation_page()
    return qiwa_api


def login_and_open_delegation_dashboard_page(personal_number: str, sequence_number: int | str):
    qiwa_api = QiwaApi.login_as_user(personal_number=personal_number).select_company(
        sequence_number=int(sequence_number)
    )
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_delegation_dashboard_page()
    set_cookies_for_browser(cookies)
    qiwa.delegation_dashboard_page.wait_delegation_dashboard_page_to_load().select_english_localization_on_delegation_dashboard()
    return qiwa_api


def get_partners_data(partners: list):
    partner_data = []
    for partner in partners:
        partner_name = partner["partyName"]
        partner_mobile = partner["partyMobile"]
        partner_phone_valid = partner["validPhoneNumber"]

        if partner_phone_valid is True:
            partner_phone_valid = "Verified"
        else:
            partner_phone_valid = "All partners must have a verified phone number"

        data = [partner_name, partner_mobile, partner_phone_valid]
        partner_data.append(data)
    return partner_data


def get_random_employee(employee_list):
    random_index = random.randrange(employee_list["totalElements"])
    return employee_list["content"][random_index]


def get_months_list(max_months: int):
    return [f"{i} month" if i == 1 else f"{i} months" for i in range(1, max_months + 1)]
