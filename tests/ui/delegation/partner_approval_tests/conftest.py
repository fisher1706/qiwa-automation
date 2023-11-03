from data.delegation import general_data
from src.api.app import QiwaApi
from src.ui.qiwa import qiwa
from tests.ui.delegation.conftest import (
    create_delegation_and_get_request,
    get_formatted_phone_number,
    get_partner_approval_url,
    open_url_from_sms,
)
from utils.assertion import assert_that


def get_partner_phone_number(phone_number: str) -> str:
    formatted_phone = get_formatted_phone_number(phone_number)
    return formatted_phone.replace("X", "*")


def prepare_data_for_partner_approval_flow(
    qiwa_api: QiwaApi, employee_nid: str, duration: int
) -> dict:
    headers = qiwa_api.delegation_api.set_headers()
    delegation_data = create_delegation_and_get_request(
        qiwa_api=qiwa_api,
        headers=headers,
        status=general_data.PENDING,
        employee_nid=employee_nid,
        duration=duration,
    )
    formatted_phone_number = get_partner_phone_number(
        phone_number=delegation_data["hiddenPartnerPhone"]
    )
    partner_approval_url = get_partner_approval_url(
        request_id=delegation_data["requestId"],
        phone_number_for_url=delegation_data["hiddenPartnerPhone"],
    )
    open_url_from_sms(partner_approval_url)
    qiwa.delegation_localisation.select_english_localisation_for_public_pages()
    qiwa.delegation_partner_approval_page.wait_partner_approval_page_to_load()
    prepared_data = {
        "delegationId": delegation_data["delegationId"],
        "employeeName": delegation_data["employeeName"],
        "employeeJob": delegation_data["employeeJob"],
        "employeeNid": delegation_data["employeeNid"],
        "delegationPermission": delegation_data["delegationPermission"],
        "entityName": delegation_data["entityName"],
        "partnerPhoneNumber": delegation_data["partnerPhoneNumber"],
        "formattedPhoneNumber": formatted_phone_number,
    }
    return prepared_data


def check_updated_delegation_status(qiwa_api: QiwaApi, delegation_id: int, expected_status: str):
    headers = qiwa_api.delegation_api.set_headers()
    delegation_status = qiwa_api.delegation_api.get_delegation_by_id(
        headers, delegation_id
    ).delegation_status
    assert_that(delegation_status).equals_to(expected_status)
