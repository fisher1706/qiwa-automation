import allure

from data.constants import Language
from data.lo.constants import (
    AppointmentsHistoryStatus,
    AppointmentsUser,
    OfficesInfo,
    ServicesInfo,
)
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@allure.title("Appointments: Book with visit type Establishment")
@case_id(22132)
def test_book_establishment_appointment():
    # todo: add arabic language support
    qiwa.login_as_user(login=AppointmentsUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.open_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()
    qiwa.labor_office_appointments_create_page.select_service(
        ServicesInfo.SERVICE_NAME_INDIVIDUALS
    )
    qiwa.labor_office_appointments_create_page.select_sub_service(
        ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS
    )
    qiwa.labor_office_appointments_create_page.click_next_step_button()
    qiwa.labor_office_appointments_create_page.select_region(OfficesInfo.REGION_MADINAH)
    qiwa.labor_office_appointments_create_page.select_office(OfficesInfo.OFFICE_NAME_VEUM_HANE)
    qiwa.labor_office_appointments_create_page.select_date()
    qiwa.labor_office_appointments_create_page.select_time()
    qiwa.labor_office_appointments_create_page.click_next_step_button()
    qiwa.labor_office_appointments_create_page.click_next_step_button()
    qiwa.labor_office_appointments_create_confirmation_page.should_success_book_message_be_visible()
    qiwa.labor_office_appointments_create_confirmation_page.should_print_button_be_visible()
    qiwa.labor_office_appointments_create_confirmation_page.should_confirmation_service_name_be(
        ServicesInfo.SERVICE_NAME_INDIVIDUALS
    )
    qiwa.labor_office_appointments_create_confirmation_page.should_confirmation_sub_service_name_be(
        ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS
    )
    qiwa.labor_office_appointments_create_confirmation_page.should_confirmation_office_name_be(
        OfficesInfo.OFFICE_NAME_VEUM_HANE
    )
    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()
    qiwa.labor_office_appointments_page.should_active_appointment_be_visible()


@allure.title("View the Appointment details (from the 'Upcoming appointments' table)")
@case_id(25509)
# @pytest.mark.parametrize("language", (Language.EN, Language.AR))
def test_view_establishment_appointment_from_upcoming():
    language = Language.EN
    # todo: add arabic language support for test_book_establishment_appointment
    # todo: this test is have support  but failed cause booking is not support
    test_book_establishment_appointment()
    qiwa.labor_office_appointments_page.view_active_appointment()
    qiwa.labor_office_appointments_view_page.language = language
    qiwa.labor_office_appointments_view_page.verify_general_info_row()
    qiwa.labor_office_appointments_view_page.verify_general_table()
    qiwa.labor_office_appointments_view_page.verify_requester_info()
    qiwa.labor_office_appointments_view_page.verify_map_elements()
    qiwa.labor_office_appointments_view_page.verify_map_functions()
    qiwa.labor_office_appointments_view_page.verify_print_btn()


@allure.title("View the Appointment details (form the 'Appointment history' table)")
@case_id(71435)
# @pytest.mark.parametrize("language", (Language.EN, Language.AR))
def test_view_establishment_appointment_from_history():
    language = Language.EN
    # todo: add arabic language support for test_book_establishment_appointment
    # todo: this test is have support  but failed cause booking is not support
    test_book_establishment_appointment()
    qiwa.labor_office_appointments_page.view_appointment_from_history_last()
    qiwa.labor_office_appointments_view_page.language = language
    qiwa.labor_office_appointments_view_page.verify_general_info_row()
    qiwa.labor_office_appointments_view_page.verify_general_table()
    qiwa.labor_office_appointments_view_page.verify_requester_info()
    qiwa.labor_office_appointments_view_page.verify_map_elements()
    qiwa.labor_office_appointments_view_page.verify_map_functions()
    qiwa.labor_office_appointments_view_page.verify_print_btn()


@allure.title("Appointments: View appointments list")
@case_id(22142)
def test_view_appointments_list():
    qiwa.login_as_user(login=AppointmentsUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.labor_office_appointments_page.navigate_to_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.should_upcoming_appointments_section_be_visible()
    qiwa.labor_office_appointments_page.should_appointments_history_section_be_visible()
    qiwa.labor_office_appointments_page.navigate_to_appointments_history()
    qiwa.labor_office_appointments_page.should_search_history_be_visible()
    qiwa.labor_office_appointments_page.should_status_filter_be_visible()
    qiwa.labor_office_appointments_page.should_history_table_headers_have_correct_titles()
    qiwa.labor_office_appointments_page.search_appointments(
        AppointmentsUser.APPOINTMENT_TO_SEARCH_IN_HISTORY
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=2, value=AppointmentsUser.APPOINTMENT_TO_SEARCH_IN_HISTORY
    )
    qiwa.labor_office_appointments_page.click_clear_search()
    qiwa.labor_office_appointments_page.search_appointments(
        AppointmentsUser.NON_EXISTING_APPOINTMENT
    )
    qiwa.labor_office_appointments_page.should_history_search_results_be_empty()
    qiwa.labor_office_appointments_page.click_clear_search()
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.Expired
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=6, value=AppointmentsHistoryStatus.Expired.name
    )
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.Cancelled
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=6, value=AppointmentsHistoryStatus.Cancelled.name
    )
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.Attended
    )
    qiwa.labor_office_appointments_page.should_history_search_results_be_empty()
    qiwa.labor_office_appointments_page.filter_appointments_history_by_status(
        AppointmentsHistoryStatus.Done
    )
    qiwa.labor_office_appointments_page.should_history_search_results_have(
        by_index=6, value=AppointmentsHistoryStatus.Done.name
    )
    qiwa.labor_office_appointments_page.navigate_to_knowledge_center()
    qiwa.labor_office_appointments_page.should_new_tab_knowledge_center_be_opened()
