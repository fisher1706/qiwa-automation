import allure

from data.constants import Language
from data.lo.constants import IndividualService, IndividualUser
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@allure.title("Appointments: View appointments list")
@case_id(39179)
def test_view_appointments_page():
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS)
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.should_history_table_headers_have_correct_titles()
    qiwa.labor_office_appointments_page.click_appointments_history_next_page()
    qiwa.labor_office_appointments_page.verify_appointments_history_next_button()
    qiwa.labor_office_appointments_page.verify_appointments_history_previous_button()
    qiwa.labor_office_appointments_page.click_appointments_history_previous_page()
    qiwa.labor_office_appointments_page.verify_appointments_history_next_button()
    qiwa.labor_office_appointments_page.navigate_to_knowledge_center()
    qiwa.labor_office_appointments_page.should_new_tab_knowledge_center_be_opened()
