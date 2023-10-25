from data.delegation import general_data
from data.delegation.delegation_data import AllDelegations, DelegationDetails
from src.api.app import QiwaApi
from tests.ui.delegation.conftest import open_delegation_details_page


def login_and_open_delegation_details_page_by_status(
    personal_number: str, sequence_number: int | str, status: str
) -> AllDelegations:
    qiwa_api = QiwaApi.login_as_user(personal_number=personal_number).select_company(
        sequence_number=int(sequence_number)
    )
    headers = qiwa_api.delegation_api.set_headers()
    delegation_list = qiwa_api.delegation_api.get_delegations_by_status(headers, status_en=status)
    open_delegation_details_page(qiwa_api, delegation_list.first_delegation_id)
    return delegation_list


def login_and_open_delegation_details_page(
    personal_number: str, sequence_number: int | str
) -> DelegationDetails:
    qiwa_api = QiwaApi.login_as_user(personal_number=personal_number).select_company(
        sequence_number=int(sequence_number)
    )
    headers = qiwa_api.delegation_api.set_headers()
    delegation_list = qiwa_api.delegation_api.get_delegations(headers)
    delegation_details = qiwa_api.delegation_api.get_delegation_by_id(
        headers, delegation_list.first_delegation_id
    )
    open_delegation_details_page(qiwa_api, delegation_list.first_delegation_id)
    return delegation_details


def formatted_phone_number(phone_number: str) -> str:
    return f"{phone_number[:4]} {phone_number[4:6]} {phone_number[6:9]} {phone_number[9:]}"


def get_partners_names_for_delegation_details(partner_list: list) -> list:
    partner_names = []
    for partner in partner_list:
        partner_names.append(partner["partnerName"])
    return partner_names


def get_partners_phone_numbers_for_delegation_details(partner_list: list) -> list:
    partners_numbers = []
    for partner in partner_list:
        partner_phone = partner["partnerPhoneNumber"]
        formatted_partner_phone_number = formatted_phone_number(partner_phone)
        partners_numbers.append(formatted_partner_phone_number)
    return partners_numbers


def get_partners_request_status_for_delegation_details(partner_list: list) -> list:
    partner_request_statuses = []
    for partner in partner_list:
        if partner["status"] == general_data.PENDING:
            expected_status = general_data.PENDING_REQUEST
        else:
            expected_status = partner["status"].capitalize()
        partner_request_statuses.append(expected_status)
    return partner_request_statuses
