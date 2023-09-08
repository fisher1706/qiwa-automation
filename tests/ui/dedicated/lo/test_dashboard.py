import allure
import pytest

from data.constants import Language
from data.dedicated.change_occupation import lo_co_user_1
from data.dedicated.enums import SearchingType
from src.api.app import QiwaApi
from src.api.controllers.ibm import IBMApiController
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@pytest.fixture(autouse=True)
def pre_test():
    api = QiwaApi.login_as_user(lo_co_user_1.personal_number)
    api.visits_api.cancel_active_visit(lo_co_user_1.personal_number)


@allure.title("Test dashboard")
@case_id(32963)
def test_dashboard():
    appointment_id = IBMApiController().create_new_appointment(lo_co_user_1)
    qiwa.login_as_user(login=lo_co_user_1.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.visits_page.click_on_proceed_button()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.appointment_page.execute()
    qiwa.work_permit_page.verify_wp_dashboard_title(
        "WORK PERMITS - Select employees for issuing or renewal of work permit") \
        .verify_wp_requests_service() \
        .click_on_back_to_wp() \
        .verify_wp_debts_service() \
        .click_on_back_to_wp() \
        .verify_show_employee_btns() \
        .verify_total_results()
