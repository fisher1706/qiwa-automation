import allure

from src.ui.qiwa import qiwa


@allure.title("User sign in to Qiwa SSO")
def test_check_login_try_sso(owner_module):
    personal_date = owner_module
    qiwa.login_as_new_user(login=personal_date.personal_number) \
        .workspace_page.select_first_company_account()
