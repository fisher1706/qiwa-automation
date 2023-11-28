import allure
import pytest

import utils.helpers
from data.constants import AppointmentReason, Language
from data.lo.constants import (
    AppointmentsHistoryStatus,
    IndividualService,
    IndividualUser,
    OfficesInfo,
    ServicesInfo,
    SubscribedUser,
)
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@allure.title("Appointments[Individual]: View appointments list")
@case_id(39179)
def test_view_appointments_page():
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS[Language.EN])
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.should_history_table_headers_have_correct_titles()
    qiwa.labor_office_appointments_page.click_appointments_history_next_page()
    qiwa.labor_office_appointments_page.verify_appointments_history_next_button()
    qiwa.labor_office_appointments_page.verify_appointments_history_previous_button()
    qiwa.labor_office_appointments_page.click_appointments_history_previous_page()
    qiwa.labor_office_appointments_page.verify_appointments_history_next_button()
    qiwa.labor_office_appointments_page.navigate_to_knowledge_center()
    qiwa.labor_office_appointments_page.should_new_tab_knowledge_center_be_opened()


@allure.title("Appointments[Individual]: Book appointment")
@case_id(39180, 54992)
@pytest.mark.parametrize("language", (Language.EN, Language.AR))
def test_book_individual_appointment(language):
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.language = language
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(language)
    qiwa.open_labor_office_appointments_page_individual()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS[language])
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()
    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_INDIVIDUALS[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS[language],
        region=OfficesInfo.REGION_MADINAH[language],
        office=OfficesInfo.OFFICE_NAME_VEUM_HANE,
    )
    qiwa.labor_office_appointments_create_confirmation_page.check_booked_appointment(
        service=ServicesInfo.SERVICE_NAME_INDIVIDUALS[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS[language],
        office=OfficesInfo.OFFICE_NAME_VEUM_HANE,
    )
    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()
    qiwa.labor_office_appointments_page.should_active_appointment_be_visible()


@allure.title("Appointments[Individual]: View details via appointments history")
@case_id(41776)
def test_individual_view_appointment_from_history():
    qiwa.login_as_user(login=SubscribedUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS[Language.EN])
    qiwa.labor_office_appointments_page.wait_page_to_load()

    qiwa.labor_office_appointments_page.search_appointments("35778")
    qiwa.labor_office_appointments_page.view_appointment_from_history_last()
    qiwa.labor_office_appointments_view_page.verify_general_info_row()
    qiwa.labor_office_appointments_view_page.verify_general_table()
    qiwa.labor_office_appointments_view_page.verify_requester_info()
    qiwa.labor_office_appointments_view_page.verify_map_elements()
    qiwa.labor_office_appointments_view_page.verify_map_functions()
    qiwa.labor_office_appointments_view_page.verify_print_btn()


@allure.title("Appointments[Individual]: Filter appointments in appointments history")
@case_id(39204)
def test_individual_filter_appointments_history():
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS[Language.EN])
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.search_appointments(
        IndividualUser.APPOINTMENT_TO_SEARCH_IN_HISTORY
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=2, value=IndividualUser.APPOINTMENT_TO_SEARCH_IN_HISTORY
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
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.UNDER_PROGRESS["index"]
    )
    qiwa.labor_office_appointments_page.should_history_search_results_be_empty()

    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.PENDING["index"]
    )
    qiwa.labor_office_appointments_page.should_history_search_results_be_empty()
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.SHOW_ALL["index"]
    )
    qiwa.labor_office_appointments_page.should_search_history_be_visible()


@allure.title("Appointments[Individual]: Multiple filter appointments in appointments history")
@case_id(39219)
def test_individual_multiple_filter_appointments_history():
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS[Language.EN])
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.EXPIRED["index"]
    )
    qiwa.labor_office_appointments_page.search_appointments(IndividualUser.APPOINTMENT_EXPIRED)
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=2, value=IndividualUser.APPOINTMENT_EXPIRED
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=6, value=AppointmentsHistoryStatus.EXPIRED["value"]
    )
    qiwa.labor_office_appointments_page.click_clear_search()

    # check cancelled appointments multiple filter
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.CANCELLED["index"]
    )
    qiwa.labor_office_appointments_page.search_appointments(IndividualUser.APPOINTMENT_CANCELLED)
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=2, value=IndividualUser.APPOINTMENT_CANCELLED
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=6, value=AppointmentsHistoryStatus.CANCELLED["value"]
    )
    qiwa.labor_office_appointments_page.click_clear_search()

    # check attended appointments multiple filter
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.ATTENDED["index"]
    )
    qiwa.labor_office_appointments_page.search_appointments(IndividualUser.APPOINTMENT_ATTENDED)
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=2, value=IndividualUser.APPOINTMENT_ATTENDED
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=6, value=AppointmentsHistoryStatus.ATTENDED["value"]
    )
    qiwa.labor_office_appointments_page.click_clear_search()

    # check done appointments multiple filter
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.DONE["index"]
    )
    qiwa.labor_office_appointments_page.search_appointments(IndividualUser.APPOINTMENT_DONE)
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=2, value=IndividualUser.APPOINTMENT_DONE
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=6, value=AppointmentsHistoryStatus.DONE["value"]
    )


@allure.title("Appointments[Individual]: View details via upcoming appointments")
@case_id(43167)
def test_individual_view_appointment_from_upcoming():
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS[Language.EN])
    qiwa.labor_office_appointments_page.wait_page_to_load()

    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_INDIVIDUALS[Language.EN],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS[Language.EN],
        region=OfficesInfo.REGION_MADINAH[Language.EN],
        office=OfficesInfo.OFFICE_NAME_VEUM_HANE,
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


@allure.title(
    "Appointments[Individual]: Cancel Appointment (from the 'Upcoming appointments' table)"
)
@case_id(41845)
def test_individual_cancel_appointment_from_active_appointments():
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS[Language.EN])
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_INDIVIDUALS[Language.EN],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS[Language.EN],
        region=OfficesInfo.REGION_MADINAH[Language.EN],
        office=OfficesInfo.OFFICE_NAME_VEUM_HANE,
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


@allure.title("Appointments[Individual]: Cancel Appointment (from the 'Appointment details' page)")
@case_id(41854)
def test_individual_cancel_appointment_from_details_appointments():
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS[Language.EN])
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_INDIVIDUALS[Language.EN],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS[Language.EN],
        region=OfficesInfo.REGION_MADINAH[Language.EN],
        office=OfficesInfo.OFFICE_NAME_VEUM_HANE,
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


@allure.title("Appointments[Individual]: As LO User I have possibility to Edit Appointment")
@case_id(43425)
def test_individual_edit_appointment():
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS[Language.EN])
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_INDIVIDUALS[Language.EN],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS[Language.EN],
        region=OfficesInfo.REGION_MADINAH[Language.EN],
        office=OfficesInfo.OFFICE_NAME_VEUM_HANE,
    )

    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()

    qiwa.labor_office_appointments_page.check_context_action_menu_from_upcoming()
    qiwa.labor_office_appointments_page.edit_active_appointment()

    qiwa.labor_office_appointments_edit_page.open_knowledge_center()
    qiwa.labor_office_appointments_edit_page.verify_knowledge_center_page_load()
    utils.helpers.scroll_to_coordinates()
    qiwa.labor_office_appointments_edit_page.change_details_fields(
        region=OfficesInfo.REGION_MADINAH[Language.EN], office=OfficesInfo.OFFICE_NAME_VEUM_HANE
    )
    qiwa.labor_office_appointments_edit_page.next_step_btn_click()

    qiwa.labor_office_appointments_edit_page.verify_summary_table(
        office_name=OfficesInfo.OFFICE_NAME_VEUM_HANE, type_value="In-person"
    )
    qiwa.labor_office_appointments_edit_page.book_app_btn_click()

    qiwa.labor_office_appointments_create_confirmation_page.check_booked_appointment(
        service=ServicesInfo.SERVICE_NAME_INDIVIDUALS[Language.EN],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS[Language.EN],
        office=OfficesInfo.OFFICE_NAME_VEUM_HANE,
    )
    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()

    qiwa.labor_office_appointments_page.check_active_appointment_exist()

    qiwa.labor_office_appointments_page.view_active_appointment()
    qiwa.labor_office_appointments_view_page.verify_general_info_row()
    qiwa.labor_office_appointments_view_page.verify_general_table()
    qiwa.labor_office_appointments_view_page.verify_requester_info()


@allure.title(
    "Appointments[Individual]: As LO User I see validation message when book appointment once exists"
)
@case_id(43426)
def test_individual_verify_validation_error_on_book_appointment_once_exists():
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS[Language.EN])
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_INDIVIDUALS[Language.EN],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS[Language.EN],
        region=OfficesInfo.REGION_MADINAH[Language.EN],
        office=OfficesInfo.OFFICE_NAME_VEUM_HANE,
    )
    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()

    qiwa.labor_office_appointments_page.click_book_appointment_btn()
    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_INDIVIDUALS[Language.EN],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS[Language.EN],
        region=OfficesInfo.REGION_MADINAH[Language.EN],
        office=OfficesInfo.OFFICE_NAME_VEUM_HANE,
    )
    qiwa.labor_office_appointments_create_page.should_validation_additional_appointment_be()
