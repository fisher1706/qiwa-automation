import allure
import pytest

from data.constants import Language
from data.dedicated.employee_list.employee_list_users import employer
from data.dedicated.employee_list.employee_transfer_constants import SearchBy
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.EMPLOYEE_LIST)


@case_id(17761, 17764, 17765, 17766, 17768, 17762, 17769, 17773, 17772, 20723, 20724)
@pytest.mark.parametrize(
    "by, text",
    [
        (SearchBy.EMPLOYEE_NAME, "Aamir"),
        (SearchBy.EMPLOYEE_NAME, "Rahman"),
        (SearchBy.EMPLOYEE_NAME, "Ali"),
        (SearchBy.EMPLOYEE_NAME, "Sadiq"),
        (SearchBy.EMPLOYEE_NAME, "احمد"),
        (SearchBy.EMPLOYEE_NAME, "أمل عبدالواحد احمد"),
        (SearchBy.EMPLOYEE_NAME, "آل عبدالواحد"),
        (SearchBy.EMPLOYEE_NAME, "AHMED FAROOQ"),
        (SearchBy.EMPLOYEE_NAME, "HAMID FAROOQ"),
        (SearchBy.EMPLOYEE_ID, "1356"),
        (SearchBy.EMPLOYEE_ID, "2288376730"),
        pytest.param(SearchBy.EMPLOYEE_ID, "2288376730", marks=[pytest.mark.skip]),
        (SearchBy.NATIONALITY, "Saudi"),
        (SearchBy.OCCUPATION, "محلل مالي"),
    ],
    ids=[
        "Valid First Name Search",
        "Valid Second Name Search",
        "Valid Third Name Search",
        "Valid Fourth Name Search",
        "Valid Search in Arabic",
        "Valid Search in Arabic first name",
        "Valid Search in Arabic last name",
        "Valid Search in English first name",
        "Valid Search in English last name",
        "Valid National Number Search",
        "Valid Iqama Number Search",
        "Valid Border Number Search",
        "Valid Nationality Search",
        "Valid Occupation Search",
    ]
)
def test_search_functionality_works_correctly_when_searching_employees(by, text):
    qiwa.login_as_user(employer.personal_number)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_company_account_with_sequence_number(employer.sequence_number)

    qiwa.dashboard_page.wait_dashboard_page_to_load()
    qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
    qiwa.open_employee_list_page()
    qiwa.employee_list_page.search(by, text)


@case_id(17770, 17771)
@pytest.mark.parametrize(
    "text",
    ["Non-existing", "1234567890"],
    ids=[
        "Search by Non-existing Name",
        "Search by Non-existing number"
    ]
)
def test_search_non_existing_user(text):
    qiwa.login_as_user(employer.personal_number)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_company_account_with_sequence_number(employer.sequence_number)

    qiwa.dashboard_page.wait_dashboard_page_to_load()
    qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
    qiwa.open_employee_list_page()
    qiwa.employee_list_page.verify_nothing_was_found_message(text)


@allure.title("Search with Empty Field")
@case_id(17763)
def test_search_with_empty_field():
    qiwa.login_as_user(employer.personal_number)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_company_account_with_sequence_number(employer.sequence_number)

    qiwa.dashboard_page.wait_dashboard_page_to_load()
    qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
    qiwa.open_employee_list_page()
    user_ids = qiwa.employee_list_page.get_users_ids_from_table()
    qiwa.employee_list_page.fill_random_search_and_clear()
    qiwa.employee_list_page.verify_user_ids(user_ids)
