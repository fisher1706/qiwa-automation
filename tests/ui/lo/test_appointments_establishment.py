import allure
import pytest

import utils.helpers
from data.constants import AppointmentReason, Language
from data.lo.constants import (
    AppointmentsHistoryStatus,
    OfficesInfo,
    ServicesInfo,
    SubscribedUser,
    UnSubscribedUser,
)
from data.lo.data_set import Case22173ServiceList
from src.api.assertions.lo import (
    assert_eligible_workspace_establishments,
    assert_non_eligible_workspace_establishments,
    assert_user_eligible_services_contains_required_ids,
)
from src.api.controllers.ibm import IBMApiController
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@allure.title("Appointments: Book with visit type Establishment")
@case_id(22132, 54971)
@pytest.mark.parametrize("language", (Language.EN, Language.AR))
def test_book_establishment_appointment(language):
    qiwa.login_as_user(login=SubscribedUser.ID)
    qiwa.workspace_page.language = language
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(language)
    qiwa.workspace_page.select_company_account_with_sequence_number(SubscribedUser.SEQUENCE_NUMBER)
    qiwa.open_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_WORK_PERMITS[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_RENEW_WORK_PERMITS[language],
        region=OfficesInfo.REGION_MADINAH[language],
        office=OfficesInfo.OFFICE_NAME_TEST_OFFICE,
        establishment=SubscribedUser.ESTABLISHMENT[language],
    )
    qiwa.labor_office_appointments_create_confirmation_page.check_booked_appointment(
        service=ServicesInfo.SERVICE_NAME_WORK_PERMITS[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_RENEW_WORK_PERMITS[language],
        office=OfficesInfo.OFFICE_NAME_TEST_OFFICE,
    )
    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()
    qiwa.labor_office_appointments_page.should_active_appointment_be_visible()


@allure.title("Appointments: View the Appointment details from the 'Upcoming appointments' table")
@case_id(25509)
def test_view_establishment_appointment_from_upcoming(language=Language.EN):
    qiwa.login_as_user(login=SubscribedUser.ID)
    qiwa.workspace_page.language = language
    qiwa.labor_office_appointments_view_page.language = language

    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(language)
    qiwa.workspace_page.select_company_account_with_sequence_number(SubscribedUser.SEQUENCE_NUMBER)
    qiwa.open_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_WORK_PERMITS[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_RENEW_WORK_PERMITS[language],
        region=OfficesInfo.REGION_MADINAH[language],
        office=OfficesInfo.OFFICE_NAME_TEST_OFFICE,
        establishment=SubscribedUser.ESTABLISHMENT[language],
    )

    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()
    qiwa.labor_office_appointments_page.should_active_appointment_be_visible()

    qiwa.labor_office_appointments_page.view_active_appointment()
    qiwa.labor_office_appointments_view_page.verify_general_info_row()
    qiwa.labor_office_appointments_view_page.verify_general_table()
    qiwa.labor_office_appointments_view_page.verify_requester_info()
    qiwa.labor_office_appointments_view_page.verify_map_elements()
    qiwa.labor_office_appointments_view_page.verify_map_functions()
    qiwa.labor_office_appointments_view_page.verify_print_btn()


@allure.title("Appointments: View the Appointment details (from the 'Appointment history' table)")
@case_id(71435)
def test_view_establishment_appointment_from_history(language=Language.EN):
    qiwa.login_as_user(login=SubscribedUser.ID)
    qiwa.workspace_page.language = language
    qiwa.labor_office_appointments_view_page.language = language

    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(language)
    qiwa.workspace_page.select_company_account_with_sequence_number(SubscribedUser.SEQUENCE_NUMBER)
    qiwa.open_labor_office_appointments_page()

    qiwa.labor_office_appointments_page.view_appointment_from_history_last()
    qiwa.labor_office_appointments_view_page.verify_general_info_row()
    qiwa.labor_office_appointments_view_page.verify_general_table()
    qiwa.labor_office_appointments_view_page.verify_requester_info()
    qiwa.labor_office_appointments_view_page.verify_map_elements()
    qiwa.labor_office_appointments_view_page.verify_map_functions()
    qiwa.labor_office_appointments_view_page.verify_print_btn()


@allure.title("Appointments: View appointments list")
@case_id(22142)
def test_view_appointments_list():
    qiwa.login_as_user(login=SubscribedUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_company_account_with_sequence_number(SubscribedUser.SEQUENCE_NUMBER)
    qiwa.open_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.should_upcoming_appointments_section_be_visible()
    qiwa.labor_office_appointments_page.should_appointments_history_section_be_visible()
    qiwa.labor_office_appointments_page.navigate_to_appointments_history()
    qiwa.labor_office_appointments_page.should_search_history_be_visible()
    qiwa.labor_office_appointments_page.should_status_filter_be_visible()
    qiwa.labor_office_appointments_page.should_history_table_headers_have_correct_titles()
    qiwa.labor_office_appointments_page.search_appointments(
        SubscribedUser.APPOINTMENT_TO_SEARCH_IN_HISTORY
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=2, value=SubscribedUser.APPOINTMENT_TO_SEARCH_IN_HISTORY
    )
    qiwa.labor_office_appointments_page.click_clear_search()
    qiwa.labor_office_appointments_page.search_appointments(
        SubscribedUser.NON_EXISTING_APPOINTMENT
    )
    qiwa.labor_office_appointments_page.should_history_search_results_be_empty()
    qiwa.labor_office_appointments_page.click_clear_search()
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.EXPIRED["index"]
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=6, value=AppointmentsHistoryStatus.EXPIRED["value"]
    )
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.CANCELLED["index"]
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=6, value=AppointmentsHistoryStatus.CANCELLED["value"]
    )
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.ATTENDED["index"]
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=6, value=AppointmentsHistoryStatus.ATTENDED["value"]
    )
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.DONE["index"]
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=6, value=AppointmentsHistoryStatus.DONE["value"]
    )
    qiwa.labor_office_appointments_page.navigate_to_knowledge_center()
    qiwa.labor_office_appointments_page.should_new_tab_knowledge_center_be_opened()


@allure.title("Appointments: View service list as subscribed user")
@case_id(22173)
def test_view_service_list_subscribed_user():
    ibm = IBMApiController()
    qiwa.login_as_user(login=SubscribedUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_company_account_with_sequence_number(SubscribedUser.SEQUENCE_NUMBER)
    workspace_establishments = ibm.get_workspace_establishments(id_no=SubscribedUser.ID)
    assert_eligible_workspace_establishments(workspace_establishments)
    assert_non_eligible_workspace_establishments(workspace_establishments)
    qiwa.open_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()
    qiwa.labor_office_appointments_create_page.select_establishment(
        SubscribedUser.ESTABLISHMENT[Language.EN]
    )
    qiwa.labor_office_appointments_create_page.select_appointment_reason(
        AppointmentReason.IN_PERSON
    )
    qiwa.labor_office_appointments_create_page.dropdown_select_service.expand()
    qiwa.labor_office_appointments_create_page.should_service_list_be()
    response = ibm.get_user_eligible_services(
        id_no=SubscribedUser.ID,
        office_id=SubscribedUser.OFFICE_ID,
        sequence=SubscribedUser.ESTABLISHMENT_SEQUENCE,
    )
    assert_user_eligible_services_contains_required_ids(
        actual=[
            x.Service.Service
            for x in response.GetUserEligibleServicesRs.Body.EligibleServicesList.EligibleServicesItem
        ],
        expected=[
            Case22173ServiceList.WORK_PERMIT,
            Case22173ServiceList.EMPLOYEE_TRANSFER,
            Case22173ServiceList.VISA,
            Case22173ServiceList.SC,
            Case22173ServiceList.POLICY,
            Case22173ServiceList.CO,
        ],
    )


@allure.title("Appointments: View service list as unsubscribed user")
@case_id(22174)
@pytest.mark.skip("Lack of test data, required specific user")
def test_view_service_list_unsubscribed_user():
    ibm = IBMApiController()
    qiwa.login_as_user(login=UnSubscribedUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_company_account_with_sequence_number(
        UnSubscribedUser.SEQUENCE_NUMBER
    )
    qiwa.dashboard_page.wait_dashboard_page_to_load()
    qiwa.open_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()
    qiwa.labor_office_appointments_create_page.select_establishment(
        UnSubscribedUser.ESTABLISHMENT[Language.EN]
    )
    qiwa.labor_office_appointments_create_page.select_appointment_reason(
        AppointmentReason.IN_PERSON
    )
    qiwa.labor_office_appointments_create_page.dropdown_select_service.expand()
    qiwa.labor_office_appointments_create_page.should_service_list_be()
    response = ibm.get_user_establishments_mlsdlo(id_no=UnSubscribedUser.ID)
    # todo add validation step to check mlsdlo response


@allure.title("Appointments: Cancel Appointment (from the 'Upcoming appointments' table)")
@case_id(22144)
def test_cancel_appointment_from_active_appointments(language=Language.EN):
    qiwa.login_as_user(login=SubscribedUser.ID)
    qiwa.workspace_page.language = language

    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(language)
    qiwa.workspace_page.select_company_account_with_sequence_number(SubscribedUser.SEQUENCE_NUMBER)
    qiwa.open_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_WORK_PERMITS[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_RENEW_WORK_PERMITS[language],
        region=OfficesInfo.REGION_MADINAH[language],
        office=OfficesInfo.OFFICE_NAME_TEST_OFFICE,
        establishment=SubscribedUser.ESTABLISHMENT[language],
    )

    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()
    qiwa.labor_office_appointments_page.should_active_appointment_be_visible()

    qiwa.labor_office_appointments_page.upcoming_appointments_actions.click()
    qiwa.labor_office_appointments_page.button_action_cancel_upcoming_appointment.click()
    qiwa.labor_office_appointments_page.verify_cancel_app_wrapper()

    qiwa.labor_office_appointments_page.cancel_app_wrapper_close_btn.click()
    qiwa.labor_office_appointments_page.should_active_appointment_be_visible()

    qiwa.labor_office_appointments_page.upcoming_appointments_actions.click()
    qiwa.labor_office_appointments_page.button_action_cancel_upcoming_appointment.click()
    qiwa.labor_office_appointments_page.verify_cancel_app_wrapper()
    qiwa.labor_office_appointments_page.cancel_app_wrapper_back_btn.click()
    qiwa.labor_office_appointments_page.should_active_appointment_be_visible()

    qiwa.labor_office_appointments_page.upcoming_appointments_actions.click()
    qiwa.labor_office_appointments_page.button_action_cancel_upcoming_appointment.click()
    qiwa.labor_office_appointments_page.verify_cancel_app_wrapper()
    qiwa.labor_office_appointments_page.cancel_app_wrapper_cancel_btn.click()
    qiwa.labor_office_appointments_page.button_close_modal.click()

    qiwa.labor_office_appointments_page.check_active_appointment_exist(exist=False)


@allure.title("Appointments: Cancel Appointment (from the 'Appointment details' page)")
@case_id(32998)
def test_cancel_appointment_from_details_appointments(language=Language.EN):
    qiwa.login_as_user(login=SubscribedUser.ID)
    qiwa.workspace_page.language = language

    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(language)
    qiwa.workspace_page.select_company_account_with_sequence_number(SubscribedUser.SEQUENCE_NUMBER)
    qiwa.open_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_WORK_PERMITS[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_RENEW_WORK_PERMITS[language],
        region=OfficesInfo.REGION_MADINAH[language],
        office=OfficesInfo.OFFICE_NAME_TEST_OFFICE,
        establishment=SubscribedUser.ESTABLISHMENT[language],
    )

    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()
    qiwa.labor_office_appointments_page.should_active_appointment_be_visible()

    qiwa.labor_office_appointments_page.view_active_appointment()
    qiwa.labor_office_appointments_view_page.cancel_btn.click()
    qiwa.labor_office_appointments_page.verify_cancel_app_wrapper()

    qiwa.labor_office_appointments_page.cancel_app_wrapper_close_btn.click()
    qiwa.labor_office_appointments_view_page.verify_general_info_row()

    qiwa.labor_office_appointments_view_page.cancel_btn.click()
    qiwa.labor_office_appointments_page.verify_cancel_app_wrapper()
    qiwa.labor_office_appointments_page.cancel_app_wrapper_back_btn.click()
    qiwa.labor_office_appointments_view_page.verify_general_info_row()

    qiwa.labor_office_appointments_view_page.cancel_btn.click()
    qiwa.labor_office_appointments_page.verify_cancel_app_wrapper()
    qiwa.labor_office_appointments_page.cancel_app_wrapper_cancel_btn.click()
    qiwa.labor_office_appointments_page.button_close_modal.click()

    qiwa.labor_office_appointments_page.check_active_appointment_exist(exist=False)


@allure.title("Appointments: As LO User I have possibility to Edit Appointment")
@case_id(22172)
def test_edit_establishment_appointment(language=Language.EN):
    qiwa.login_as_user(login=SubscribedUser.ID)
    qiwa.workspace_page.language = language
    qiwa.labor_office_appointments_view_page.language = language

    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(language)
    qiwa.workspace_page.select_company_account_with_sequence_number(SubscribedUser.SEQUENCE_NUMBER)
    qiwa.open_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_WORK_PERMITS[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_RENEW_WORK_PERMITS[language],
        region=OfficesInfo.REGION_MADINAH[language],
        office=OfficesInfo.OFFICE_NAME_TEST_OFFICE,
        establishment=SubscribedUser.ESTABLISHMENT[language],
    )

    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()

    qiwa.labor_office_appointments_page.check_context_action_menu_from_upcoming()
    qiwa.labor_office_appointments_page.edit_active_appointment()

    qiwa.labor_office_appointments_edit_page.open_knowledge_center()
    qiwa.labor_office_appointments_edit_page.verify_knowledge_center_page_load()
    qiwa.labor_office_appointments_edit_page.verify_edit_page_typical()
    qiwa.labor_office_appointments_edit_page.change_details_fields(
        region=OfficesInfo.REGION_MADINAH[language], office=OfficesInfo.OFFICE_NAME_TEST_OFFICE
    )
    qiwa.labor_office_appointments_edit_page.next_step_btn_click()

    qiwa.labor_office_appointments_edit_page.verify_summary_table(
        office_name=OfficesInfo.OFFICE_NAME_TEST_OFFICE, type_value="In-person"
    )
    qiwa.labor_office_appointments_edit_page.book_app_btn_click()

    qiwa.labor_office_appointments_create_confirmation_page.check_booked_appointment(
        service=ServicesInfo.SERVICE_NAME_WORK_PERMITS[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_RENEW_WORK_PERMITS[language],
        office=OfficesInfo.OFFICE_NAME_TEST_OFFICE,
    )
    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()

    qiwa.labor_office_appointments_page.check_active_appointment_exist()

    qiwa.labor_office_appointments_page.view_active_appointment()
    qiwa.labor_office_appointments_view_page.verify_general_info_row()
    qiwa.labor_office_appointments_view_page.verify_general_table()
    qiwa.labor_office_appointments_view_page.verify_requester_info()


@allure.title(
    "Appointments: Edit Appointment in process of booking with visit type 'Establishments'"
)
@case_id(22143)
def test_edit_establishment_appointment_from_booking(language=Language.EN):
    qiwa.login_as_user(login=SubscribedUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(language)
    qiwa.workspace_page.select_company_account_with_sequence_number(SubscribedUser.SEQUENCE_NUMBER)
    qiwa.open_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.verify_select_establishment_visible()
    qiwa.labor_office_appointments_create_page.verify_next_btn_visible()
    qiwa.labor_office_appointments_create_page.select_establishment(
        SubscribedUser.ESTABLISHMENT[language]
    )

    qiwa.labor_office_appointments_create_page.verify_appointment_reason_blocks_visible()
    qiwa.labor_office_appointments_create_page.verify_next_btn_visible()

    qiwa.labor_office_appointments_create_page.edit_creators_info_btn.click()
    qiwa.labor_office_appointments_create_page.verify_select_establishment_visible()
    qiwa.labor_office_appointments_create_page.verify_next_btn_visible()
    qiwa.labor_office_appointments_create_page.select_establishment(
        SubscribedUser.ESTABLISHMENT[language]
    )

    qiwa.labor_office_appointments_create_page.verify_appointment_reason_blocks_visible()
    qiwa.labor_office_appointments_create_page.verify_next_btn_visible()

    qiwa.labor_office_appointments_create_page.select_appointment_reason(
        AppointmentReason.IN_PERSON
    )

    qiwa.labor_office_appointments_create_page.verify_service_and_subservice_blocks_visible()
    qiwa.labor_office_appointments_create_page.verify_next_btn_visible()

    utils.helpers.scroll_to_coordinates()

    qiwa.labor_office_appointments_create_page.edit_reason_btn.click()
    qiwa.labor_office_appointments_create_page.verify_appointment_reason_blocks_visible()
    qiwa.labor_office_appointments_create_page.verify_next_btn_visible()

    qiwa.labor_office_appointments_create_page.select_appointment_reason(
        AppointmentReason.IN_PERSON
    )

    qiwa.labor_office_appointments_create_page.select_service(
        ServicesInfo.SERVICE_NAME_WORK_PERMITS[language]
    )
    qiwa.labor_office_appointments_create_page.select_sub_service(
        ServicesInfo.SUB_SERVICE_NAME_RENEW_WORK_PERMITS[language]
    )
    qiwa.labor_office_appointments_create_page.click_next_step_button()
    qiwa.labor_office_appointments_create_page.verify_appointment_details_blocks_visible()

    utils.helpers.scroll_to_coordinates()

    qiwa.labor_office_appointments_create_page.edit_service_btn.click()

    qiwa.labor_office_appointments_create_page.verify_service_and_subservice_blocks_visible()
    qiwa.labor_office_appointments_create_page.verify_next_btn_visible()
    qiwa.labor_office_appointments_create_page.click_next_step_button()

    qiwa.labor_office_appointments_create_page.select_region(OfficesInfo.REGION_MADINAH[language])
    qiwa.labor_office_appointments_create_page.select_office(OfficesInfo.OFFICE_NAME_TEST_OFFICE)
    qiwa.labor_office_appointments_create_page.select_date()
    qiwa.labor_office_appointments_create_page.select_time()
    qiwa.labor_office_appointments_create_page.click_next_step_button()
    qiwa.labor_office_appointments_create_page.verify_summary_blocks_visible()

    utils.helpers.scroll_to_coordinates()

    qiwa.labor_office_appointments_create_page.edit_details_btn.click()
    qiwa.labor_office_appointments_create_page.verify_appointment_details_blocks_visible()
    qiwa.labor_office_appointments_create_page.click_next_step_button()
    qiwa.labor_office_appointments_create_page.verify_summary_blocks_visible()

    utils.helpers.scroll_to_coordinates()

    qiwa.labor_office_appointments_create_page.edit_creators_info_btn.click()
    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_WORK_PERMITS[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_RENEW_WORK_PERMITS[language],
        region=OfficesInfo.REGION_MADINAH[language],
        office=OfficesInfo.OFFICE_NAME_TEST_OFFICE,
        establishment=SubscribedUser.ESTABLISHMENT[language],
    )

    qiwa.labor_office_appointments_create_confirmation_page.check_booked_appointment(
        service=ServicesInfo.SERVICE_NAME_WORK_PERMITS[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_RENEW_WORK_PERMITS[language],
        office=OfficesInfo.OFFICE_NAME_TEST_OFFICE,
    )
    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()

    qiwa.labor_office_appointments_page.check_context_action_menu_from_upcoming()
