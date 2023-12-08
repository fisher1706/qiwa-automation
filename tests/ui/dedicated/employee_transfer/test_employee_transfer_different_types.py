import pytest

from data.constants import Language
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
from src.ui.actions.employee_transfer import employee_transfer_actions
from src.ui.actions.individual_actions import individual_actions
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.EMPLOYEE_TRANSFER)


@pytest.mark.parametrize(
    'status',
    [
        RequestStatus.PENDING_COMPLETING_TRANSFER_IN_ABSHER_BY_NEW_EMPLOYER.value,
        RequestStatus.REJECTED_BY_CURRENT_EMPLOYER.value
    ],
    ids=[
        '[Type 12] Approval by laborer and approval by current sponsor | Home Worker Transfer',
        '[Type 12] Approval by laborer and rejection by current sponsor | Home Worker Transfer'
    ]
)
@case_id(134165, 134166)
def test_type_12_current_sponsor(status):
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_12.personal_number)
    ibm_api.create_new_contract(employer, laborer_type_12)
    ibm_api.create_employee_transfer_request_ae(employer, laborer_type_12, current_sponsor_type_12)

    employee_transfer_actions.navigate_to_individual(laborer_type_12.personal_number)

    qiwa.dashboard_page.wait_dashboard_page_to_load()
    qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
    
    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFERS.value[Language.EN]) \
        .click_agree_checkbox()

    individual_actions.approve_request()

    qiwa.header.click_on_menu_individuals().click_on_logout()

    employee_transfer_actions.navigate_to_individual(current_sponsor_type_12.personal_number)

    qiwa.individual_page.navigate_to_services()

    qiwa.individual_page.select_service(ServicesAndTools.HOME_WORKERS_TRANSFER.value[Language.EN])

    qiwa.employee_transfer_page.search_received_request(laborer_type_12.personal_number)

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
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer.personal_number)
    ibm_api.create_new_contract(employer, laborer)
    ibm_api.create_employee_transfer_request_ae(employer, laborer)

    employee_transfer_actions.navigate_to_individual(laborer.personal_number)

    qiwa.dashboard_page.wait_dashboard_page_to_load()
    qiwa.meet_qiwa_popup.close_meet_qiwa_popup()

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFERS.value[Language.EN]) \
        .click_agree_checkbox()

    individual_actions.reject_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(RequestStatus.REJECTED_BY_LABORER.value[Language.EN])
    qiwa.header.change_local(Language.AR)
    individual_actions.verify_expected_status(RequestStatus.REJECTED_BY_LABORER.value[Language.AR])


@pytest.mark.parametrize(
    "laborer, status",
    [
        (laborer_type_9, RequestStatus.PENDING_COMPLETING_TRANSFER_IN_ABSHER_BY_NEW_EMPLOYER.value),
        (laborer_type_4_freedom_transfer, RequestStatus.PENDING_FOR_NOTICE_PERIOD_COMPLETION.value),
        (laborer_type_4_direct_transfer, RequestStatus.PENDING_COMPLETING_TRANSFER_IN_ABSHER_BY_NEW_EMPLOYER.value),
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
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer.personal_number)
    ibm_api.create_new_contract(employer, laborer)
    ibm_api.create_employee_transfer_request_ae(employer, laborer)

    employee_transfer_actions.navigate_to_individual(laborer.personal_number)

    qiwa.dashboard_page.wait_dashboard_page_to_load()
    qiwa.meet_qiwa_popup.close_meet_qiwa_popup()

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
