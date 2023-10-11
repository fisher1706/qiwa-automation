import random

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


def get_months_list(max_months: int):
    return [f"{i} month" if i == 1 else f"{i} months" for i in range(1, max_months + 1)]


def get_random_employee(employee_list):
    random_index = random.randrange(employee_list["totalElements"])
    return employee_list["content"][random_index]


def formatted_phone_number(phone_number: str) -> str:
    return f"{phone_number[:4]} {phone_number[4:6]} {phone_number[6:9]} {phone_number[9:]}"


def get_partners_data_for_add_delegation(partners: list):
    partner_data = []
    for partner in partners:
        partner_name = partner["partyName"]
        partner_mobile = partner["partyMobile"]
        formatted_partner_phone = formatted_phone_number(partner_mobile)
        partner_phone_valid = partner["validPhoneNumber"]

        if partner_phone_valid is True:
            partner_phone_valid = "Verified"
        else:
            partner_phone_valid = "All partners must have a verified phone number"

        data = [partner_name, formatted_partner_phone, partner_phone_valid]
        partner_data.append(data)
    return partner_data
