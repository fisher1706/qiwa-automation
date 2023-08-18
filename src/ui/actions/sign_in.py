import allure

from data.constants import UserInfo
from src.ui.pages.login_page import LoginPage
from src.ui.pages.workspaces_page import WorkspacesPage


class LoginActions(LoginPage):
    def __init__(self):
        super().__init__()
        self.workspace_page = WorkspacesPage()

    @allure.step("Complete user login with 2fa")
    def complete_login(self, account):
        self.login_user(account.personal_number, UserInfo.PASSWORD)
        self.proceed_2fa()
        self.workspace_page.should_have_workspace_list_appear()
        return self

    @allure.step("Login user")
    def login_user(self, login, password):
        self.enter_login(login).enter_password(password).click_continue_button()
        return self

    @allure.step("Proceed two factor authentication")
    def proceed_2fa(self, two_factor_code="0000"):
        self.enter_2fa_code(two_factor_code).click_sign_in_button()
        return self
