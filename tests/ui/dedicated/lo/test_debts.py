import allure
import pytest

from data.constants import Language
from data.dedicated.change_occupation import lo_co_user_2, work_permit
from data.dedicated.enums import SearchingType
from src.api.app import QiwaApi
from src.api.controllers.ibm import IBMApiController
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@pytest.fixture(autouse=True)
def pre_test():
    api = QiwaApi.login_as_user(lo_co_user_2.personal_number)
    api.visits_api.cancel_active_visit(lo_co_user_2.personal_number)


@allure.title('AS-305 Verify that the list of debts is available for the user')
@case_id(32976)
def test_verify_that_the_list_of_debts_is_available_for_the_user():
    appointment_id = IBMApiController().create_new_appointment(lo_co_user_2, work_permit)
    qiwa.login_as_user(login=lo_co_user_2.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.visits_page.click_on_proceed_button()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.appointment_page.execute()
    qiwa.work_permit_page.verify_wp_debts_service() \
        .verify_paid_debts() \
        .verify_unpaid_debts() \
        .click_on_back_to_wp()


@allure.title('AS-306 Verify that the user can generate a sadad bill only for debts that do not have a sadad bill '
              'number')
@case_id(32977)
def test_verify_that_the_user_can_generate_sadad_bill_only_for_debts_that_do_not_have_sadad_bill_number():
    appointment_id = IBMApiController().create_new_appointment(lo_co_user_2, work_permit)
    qiwa.login_as_user(login=lo_co_user_2.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.visits_page.click_on_proceed_button()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.appointment_page.execute()
    qiwa.work_permit_page.verify_wp_debts_service() \
        .generate_sadad_number()
    # TODO ADD METHOD FOR DELETE SADAD NUMBER
