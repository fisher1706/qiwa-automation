import allure
import pytest

from data.constants import Language
from data.lo.constants import (
    AppointmentReason,
    AppointmentsView,
    IndividualService,
    IndividualUser,
    OfficesInfo,
    ServicesInfo,
)
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@allure.title("Appointments[Individual]: Book appointment with type Virtual")
@case_id(71575, 71593)
@pytest.mark.parametrize("language", [Language.EN, Language.AR])
def test_book_virtual_appointment(language):
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
        appointment_reason=AppointmentReason.VIRTUAL['id'],
        service=ServicesInfo.SERVICE_NAME_VIRTUAL[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_VIRTUAL[language],
        region=OfficesInfo.REGION_RIYADH[language],
        office=OfficesInfo.OFFICE_NAME_VIRTUAL,
    )
    qiwa.labor_office_appointments_create_confirmation_page.check_booked_appointment(
        service=ServicesInfo.SERVICE_NAME_VIRTUAL[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_VIRTUAL[language],
        office=OfficesInfo.OFFICE_NAME_VIRTUAL,
    )
    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()
    qiwa.labor_office_appointments_page.should_active_appointment_be_visible()


@allure.title(
    "Appointments[Individual]: Cancel Virtual appointment (from the 'Upcoming appointments' table)"
)
@case_id(71579)
@pytest.mark.parametrize("language", [Language.EN])
def test_individual_cancel_virtual_appointment_from_active_appointments(language):
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(language)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS[language])
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.VIRTUAL['id'],
        service=ServicesInfo.SERVICE_NAME_VIRTUAL[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_VIRTUAL[language],
        region=OfficesInfo.REGION_RIYADH[language],
        office=OfficesInfo.OFFICE_NAME_VIRTUAL,
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
    qiwa.labor_office_appointments_page.cancel_app_wrapper_cancel_btn.click()
    qiwa.labor_office_appointments_page.button_close_modal.click()

    qiwa.labor_office_appointments_page.check_active_appointment_exist(exist=False)


@allure.title("Appointments[Individual]: Cancel Virtual appointment (from the 'Appointment details' page)")
@case_id(71580)
@pytest.mark.parametrize("language", [Language.EN])
def test_individual_cancel_virtual_appointment_from_details_appointments(language):
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(language)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS[language])
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()

    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.VIRTUAL['id'],
        service=ServicesInfo.SERVICE_NAME_VIRTUAL[language],
        sub_service=ServicesInfo.SUB_SERVICE_NAME_VIRTUAL[language],
        region=OfficesInfo.REGION_RIYADH[language],
        office=OfficesInfo.OFFICE_NAME_VIRTUAL,
    )

    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()
    qiwa.labor_office_appointments_page.should_active_appointment_be_visible()

    qiwa.labor_office_appointments_page.view_active_appointment()
    qiwa.labor_office_appointments_view_page.verify_general_info_row(info=AppointmentsView.INFO_ROW_VIRTUAL_TEXT)
    qiwa.labor_office_appointments_view_page.cancel_btn.click()
    qiwa.labor_office_appointments_page.verify_cancel_app_wrapper()
    qiwa.labor_office_appointments_page.cancel_app_wrapper_cancel_btn.click()
    qiwa.labor_office_appointments_page.button_close_modal.click()

    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()
    qiwa.labor_office_appointments_page.check_active_appointment_exist(exist=False)
