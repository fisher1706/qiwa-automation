from selene import browser

from data.delegation import general_data
from src.api.app import QiwaApi
from src.database.sql_requests.delegation_requests import DelegationRequests
from src.ui.qiwa import qiwa
from utils.assertion import assert_that
from utils.helpers import set_cookies_for_browser


def login_as_establishment_owner(personal_number: str, sequence_number: int | str) -> QiwaApi:
    qiwa_api = QiwaApi.login_as_user(personal_number=personal_number).select_company(
        sequence_number=int(sequence_number)
    )
    return qiwa_api


def open_delegation_dashboard_page(qiwa_api: QiwaApi):
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_delegation_dashboard_page()
    set_cookies_for_browser(cookies)
    qiwa.delegation_dashboard_page.wait_delegation_dashboard_page_to_load().select_english_localization_on_delegation_dashboard()


def open_delegation_details_page(qiwa_api: QiwaApi, delegation_id: int):
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_delegation_details_page(delegation_id)
    set_cookies_for_browser(cookies)
    qiwa.delegation_details_page.wait_delegation_details_page_to_load().select_english_localization_on_delegation_details()


def login_and_open_delegation_dashboard_page(
    personal_number: str, sequence_number: int | str
) -> QiwaApi:
    qiwa_api = login_as_establishment_owner(
        personal_number=personal_number, sequence_number=int(sequence_number)
    )
    open_delegation_dashboard_page(qiwa_api)
    return qiwa_api


def prepare_data_for_resend_action(
    qiwa_api: QiwaApi, status: str, employee_nid: str, duration: int
) -> dict:
    headers = qiwa_api.delegation_api.set_headers()
    delegation_data = create_delegation_and_get_request(
        qiwa_api=qiwa_api,
        headers=headers,
        status=status,
        employee_nid=employee_nid,
        duration=duration,
    )
    reject_delegation_request_by_partner(
        qiwa_api=qiwa_api,
        delegation_id=delegation_data["delegationId"],
        delegation_request_id=delegation_data["requestId"],
    )
    return delegation_data


def prepare_data_for_revoke_action(qiwa_api: QiwaApi, employee_nid: str, duration: int) -> int:
    headers = qiwa_api.delegation_api.set_headers()
    delegation_id = qiwa_api.delegation_api.create_delegation(
        headers=headers, employee_nid=employee_nid, duration=duration
    )["id"]
    return delegation_id


def get_delegation_request(delegation_id: int, status: str):
    delegation_request = DelegationRequests().get_delegation_request(
        delegation_id=delegation_id, status=status
    )
    return delegation_request


def create_delegation_and_get_request(
    qiwa_api: QiwaApi, headers: dict, status: str, employee_nid: str, duration: int
) -> dict:
    delegation_id = qiwa_api.delegation_api.create_delegation(
        headers=headers, employee_nid=employee_nid, duration=duration
    )["id"]
    partner_phone_number = qiwa_api.delegation_api.get_delegation_by_id(
        headers=headers, delegation_id=delegation_id
    ).partner_list[0]["partnerPhoneNumber"]
    delegation_request = get_delegation_request(delegation_id=delegation_id, status=status)
    delegation_data = {
        "delegationId": delegation_id,
        "formattedPartnerPhone": partner_phone_number,
        "requestId": delegation_request.id,
        "partnerPhoneNumber": delegation_request.partner_phone_number,
    }
    return delegation_data


def resend_rejected_delegation_request(qiwa_api: QiwaApi, delegation_id: int):
    headers = qiwa_api.delegation_api.set_headers()
    qiwa_api.delegation_api.resend_delegation_request(headers=headers, delegation_id=delegation_id)


def reject_delegation_request_by_partner(
    qiwa_api: QiwaApi, delegation_id: int, delegation_request_id: str
):
    headers_for_public_pages = {"X-Service-Id": "delegation"}
    qiwa_api.delegation_api.get_otp_code(
        headers=headers_for_public_pages, request_id=delegation_request_id
    )
    otp_code = (
        DelegationRequests()
        .get_delegation_request(delegation_id=delegation_id, status=general_data.PENDING)
        .otp_code
    )
    headers_for_public_pages.update({"Otp-Code": otp_code})
    qiwa_api.delegation_api.reject_delegation_request(
        headers=headers_for_public_pages, request_id=delegation_request_id
    )


def check_sms_after_resend_action(
    phone_number: str,
    delegation_id: str,
    establishment_name: str,
    request_id: str,
    formatted_phone_number: str,
) -> str:
    sms_text = DelegationRequests().get_sms_request(phone_number)
    link = general_data.SMS_LINK.format(request_id, formatted_phone_number)
    expected_sms_text = f"""{general_data.SMS_TEXT.format(delegation_id, establishment_name)}
{link}"""
    assert_that(sms_text).equals_to(expected_sms_text)
    return link


def open_url_from_sms(url: str):
    browser.open(url)


def get_old_url_after_resend_action(request_id: str, formatted_phone_number: str) -> str:
    return general_data.SMS_LINK.format(request_id, formatted_phone_number)