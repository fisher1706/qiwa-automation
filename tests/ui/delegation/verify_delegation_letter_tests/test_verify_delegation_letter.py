import allure

from data.delegation import general_data
from data.delegation.users import establishment_owner_without_partners
from src.ui.qiwa import qiwa
from tests.ui.delegation.conftest import login_as_establishment_owner
from tests.ui.delegation.verify_delegation_letter_tests.conftest import (
    open_verify_delegation_letter_page,
    prepare_data_for_verify_delegation_letter,
)
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.DELEGATION)


@allure.title("Verify active delegation letter")
@case_id(57459, 57462)
def test_verify_active_delegation_letter(remove_pdf_file):
    qiwa_api = login_as_establishment_owner(
        personal_number=establishment_owner_without_partners.personal_number,
        sequence_number=establishment_owner_without_partners.sequence_number)
    headers = qiwa_api.delegation_api.set_headers()
    prepared_data = prepare_data_for_verify_delegation_letter(qiwa_api, headers)
    open_verify_delegation_letter_page()
    qiwa.delegation_letter_verify_page.upload_delegation_letter(str(prepared_data["file_path"])) \
        .should_delegation_letter_modal_be_displayed() \
        .should_values_on_delegation_letter_modal_be_correct(status=prepared_data["delegation_status"],
                                                             delegation_id=prepared_data["delegation_id"],
                                                             delegate_name=prepared_data["delegate_name"],
                                                             delegate_nid=prepared_data["delegate_nid"],
                                                             establishment=general_data.WORKSPACE_WITH_NO_PARTNERS,
                                                             expiry_date=prepared_data["expiry_date"]) \
        .click_back_to_verification_button().should_verify_delegation_letter_modal_be_closed()


@allure.title("Check error after uploading revoked delegation letter")
@case_id(57460)
def test_error_on_verify_revoked_delegation_letter(remove_pdf_file):
    qiwa_api = login_as_establishment_owner(
        personal_number=establishment_owner_without_partners.personal_number,
        sequence_number=establishment_owner_without_partners.sequence_number)
    headers = qiwa_api.delegation_api.set_headers()
    prepared_data = prepare_data_for_verify_delegation_letter(qiwa_api, headers)
    qiwa_api.delegation_api.revoke_delegation(headers, prepared_data["delegation_id"])
    open_verify_delegation_letter_page()
    qiwa.delegation_letter_verify_page.upload_delegation_letter(str(prepared_data["file_path"]))\
        .should_modal_with_error_be_displayed().click_back_to_verification_button()\
        .should_verify_delegation_letter_modal_be_closed()
