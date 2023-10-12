import allure
import pytest

from data.constants import Language, Titles
from data.dedicated.enums import SearchingType
from data.dedicated.lo_work_permit import lo_wp_user_1
from data.dedicated.models.services import lo_work_permit
from src.api.app import QiwaApi
from src.api.controllers.ibm import IBMApiController
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@pytest.fixture(autouse=True)
def pre_test():
    api = QiwaApi.login_as_user(lo_wp_user_1.personal_number)
    api.visits_api.cancel_active_visit(lo_wp_user_1.personal_number)


@allure.title('AS-269 Dashboard')
@case_id(32963)
def test_dashboard():
    appointment_id = IBMApiController().create_new_appointment(lo_wp_user_1, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_1.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.visits_page.click_on_proceed_button()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_wp_dashboard_title(Titles.WORK_PERMIT) \
        .verify_wp_requests_service() \
        .click_on_back_to_wp() \
        .verify_wp_debts_service() \
        .back_to_work_permits_from_debts() \
        .verify_show_employee_btns() \
        .verify_total_results() \
        .verify_page_pagination()
