import allure

from data.constants import Language
from data.lo.constants import OfficesInfo, ServicesInfo
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@allure.title("Appointments: Book with visit type Establishment")
@case_id(22132)
def test_book_establishment_appointment():
    qiwa.login_as_user(login="1006586984")
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.labor_office_appointments_page.navigate_to_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()
    qiwa.labor_office_appointments_create_page.select_service(ServicesInfo.SERVICE_NAME_INDIVIDUALS)
    qiwa.labor_office_appointments_create_page.select_sub_service(ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS)
    qiwa.labor_office_appointments_create_page.click_next_step_button()
    qiwa.labor_office_appointments_create_page.select_region(OfficesInfo.REGION_MADINAH)
    qiwa.labor_office_appointments_create_page.select_office(OfficesInfo.OFFICE_NAME_VEUM_HANE)
    qiwa.labor_office_appointments_create_page.select_date()
    qiwa.labor_office_appointments_create_page.select_time()
    qiwa.labor_office_appointments_create_page.click_next_step_button()
    qiwa.labor_office_appointments_create_page.click_next_step_button()
    qiwa.labor_office_appointments_create_confirmation_page.should_success_book_message_be_visible()
    qiwa.labor_office_appointments_create_confirmation_page.should_print_button_be_displayed()
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
