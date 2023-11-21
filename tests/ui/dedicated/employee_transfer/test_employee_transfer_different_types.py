import pytest

from data.constants import Language
from data.dedicated.employee_trasfer.employee_transfer_constants import (
    LABORER_STATUS_REJECT,
    LABORER_TYPE_4_DIRECT_TRANSFER_STATUS_APPROVE,
    LABORER_TYPE_4_FREEDOM_TRANSFER_STATUS_APPROVE,
    LABORER_TYPE_9_STATUS_APPROVE,
    SPONSOR_STATUS_APPROVE,
    SPONSOR_STATUS_REJECT,
)
from data.dedicated.employee_trasfer.employee_transfer_users import (
    current_sponsor_type_12,
    employer,
    laborer_type_4_absent,
    laborer_type_4_direct_transfer,
    laborer_type_4_freedom_transfer,
    laborer_type_9,
    laborer_type_12,
)
from data.dedicated.enums import RequestStatus, ServicesAndTools
from src.api.clients.employee_transfer import employee_transfer_api
from src.api.clients.ibm import ibm_api
from src.api.controllers.ibm import ibm_api_controller
from src.ui.actions.employee_transfer import employee_transfer_actions
from src.ui.actions.individual_actions import individual_actions
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.EMPLOYEE_TRANSFER)


@pytest.mark.parametrize(
    'status', [SPONSOR_STATUS_APPROVE, SPONSOR_STATUS_REJECT],
    ids=[
        '[Type 12] Approval by laborer and approval by current sponsor | Home Worker Transfer',
        '[Type 12] Approval by laborer and rejection by current sponsor | Home Worker Transfer'
    ]
)
@case_id(134165, 134166)
def test_type_12_current_sponsor(status):
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_12.login_id)
    establishment_id = ibm_api_controller.get_establishment_id(employer)
    ibm_api.create_new_contract(laborer_type_12, employer, establishment_id)

    employee_transfer_actions.navigate_to_et_service(employer)

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_another_establishment() \
        .click_btn_next_step() \
        .fill_employee_iqama_number(laborer_type_12.login_id) \
        .fill_date_of_birth(laborer_type_12.birthdate) \
        .click_btn_find_employee() \
        .click_btn_add_employee_to_transfer_request() \
        .click_btn_next_step() \
        .check_existence_of_a_contract() \
        .click_btn_next_step() \
        .select_terms_checkbox() \
        .click_btn_submit() \
        .check_request_status() \
        .click_btn_back_to_employee_transfer()

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer_type_12.login_id)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFERS.value[Language.EN]) \
        .click_agree_checkbox()

    individual_actions.approve_request()

    qiwa.header.click_on_menu_individuals().click_on_logout()

    employee_transfer_actions.navigate_to_individual(current_sponsor_type_12.personal_number)

    qiwa.individual_page.select_service(ServicesAndTools.HOME_WORKERS_TRANSFER.value)

    qiwa.employee_transfer_page.search_received_request(laborer_type_12.login_id)

    employee_transfer_actions.make_a_decision_as_current_sponsor(status)

    individual_actions.verify_expected_status(status[Language.EN])
    qiwa.header.change_local(Language.AR)
    individual_actions.verify_expected_status(status[Language.AR])


@pytest.mark.parametrize(
    'laborer', [
        laborer_type_12,
        laborer_type_9,
        laborer_type_4_freedom_transfer,
        laborer_type_4_direct_transfer,
        laborer_type_4_absent
    ],
    ids=[
        '[Type 12] Rejection by laborer | Home Worker Transfer',
        '[Type 9] Rejection by laborer | Dependent Transfer',
        '[Type 4 Freedom Transfer] Verify that after Rejection by Laborer status changes',
        '[Type 4 Direct Transfer] Verify that after Rejection by Laborer status changes',
        '[Type 4 Absent Laborer] Verify that after Rejection by Laborer status changes'
    ]
)
@case_id(134167, 134168, 134170, 134172, 134174)
def test_transfer_types_rejection_by_laborer(laborer):
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer.login_id)
    establishment_id = ibm_api_controller.get_establishment_id(employer)
    ibm_api.create_new_contract(laborer, employer, establishment_id)

    employee_transfer_actions.navigate_to_et_service(employer)

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_another_establishment() \
        .click_btn_next_step() \
        .fill_employee_iqama_number(laborer.login_id) \
        .fill_date_of_birth(laborer.birthdate) \
        .click_btn_find_employee() \
        .click_btn_add_employee_to_transfer_request() \
        .check_existence_of_a_contract() \
        .click_btn_next_step() \
        .click_btn_next_step() \
        .select_terms_checkbox() \
        .click_btn_submit() \
        .check_request_status() \
        .click_btn_back_to_employee_transfer()

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer.login_id)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFERS.value[Language.EN]) \
        .click_agree_checkbox()

    individual_actions.reject_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(LABORER_STATUS_REJECT[Language.EN])
    qiwa.header.change_local(Language.AR)
    individual_actions.verify_expected_status(LABORER_STATUS_REJECT[Language.EN])


@pytest.mark.parametrize(
    "laborer, status",
    [
        (laborer_type_9, LABORER_TYPE_9_STATUS_APPROVE),
        (laborer_type_4_freedom_transfer, LABORER_TYPE_4_FREEDOM_TRANSFER_STATUS_APPROVE),
        (laborer_type_4_direct_transfer, LABORER_TYPE_4_DIRECT_TRANSFER_STATUS_APPROVE),
        (laborer_type_4_absent, RequestStatus.PENDING_COMPLETING_TRANSFER_IN_ABSHER_BY_NEW_EMPLOYER.value)
    ],
    ids=[
        "[Type 9] Approval by laborer | Dependent Transfer",
        "[Type 4 Freedom Transfer] Verify that after Approval by Laborer status changes",
        "[Type 4 Direct Transfer] Verify that after Approval by Laborer status changes",
        "[Type 4 Absent Laborer] Verify that after Approval by Laborer status changes",
    ]
)
@case_id(134169, 134171, 134173, 134175)
def test_transfer_type_approval_by_laborer(laborer, status):
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer.login_id)
    establishment_id = ibm_api_controller.get_establishment_id(employer)
    ibm_api.create_new_contract(laborer, employer, establishment_id)

    employee_transfer_actions.navigate_to_et_service(employer)

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_another_establishment() \
        .click_btn_next_step() \
        .fill_employee_iqama_number(laborer.login_id) \
        .fill_date_of_birth(laborer.birthdate) \
        .click_btn_find_employee()

    if laborer == laborer_type_4_absent:
        qiwa.employee_transfer_page.select_late_fees_checkbox()

    qiwa.employee_transfer_page.click_btn_add_employee_to_transfer_request() \
        .check_existence_of_a_contract() \
        .click_btn_next_step() \
        .click_btn_next_step() \
        .select_terms_checkbox() \
        .click_btn_submit() \
        .check_request_status() \
        .click_btn_back_to_employee_transfer()

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer.login_id)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFERS.value[Language.EN]) \
        .click_agree_checkbox()

    individual_actions.approve_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(status[Language.EN])
    qiwa.header.change_local(Language.AR)
    individual_actions.verify_expected_status(status[Language.AR])
