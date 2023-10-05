from __future__ import annotations

import allure
from selene import be
from selene.support.shared import browser

import config
from data.constants import UserInfo
from src.api.app import QiwaApi
from src.ui.components.dedicated.email_confirmation_pop_up import EmailConfirmationPopup
from src.ui.components.feedback_pop_up import FeedbackPopup
from src.ui.components.footer import Footer
from src.ui.components.header import Header
from src.ui.pages.admin_page import AdminPage
from src.ui.pages.appointments.labor_office_appointments import (
    LaborOfficeAppointmentsPage,
)
from src.ui.pages.appointments.labor_office_appointments_create import (
    LaborOfficeAppointmentsCreatePage,
)
from src.ui.pages.appointments.labor_office_appointments_create_confirmation import (
    LaborOfficeCreateConfirmationPage,
)
from src.ui.pages.dashboard_page import DashboardPage
from src.ui.pages.dedicated_pages.appointment_request_page import AppointmentRequestPage
from src.ui.pages.dedicated_pages.business_page import BusinessPage
from src.ui.pages.dedicated_pages.change_occupation_page import ChangeOccupationPage
from src.ui.pages.dedicated_pages.requests_page import RequestsPage
from src.ui.pages.dedicated_pages.visits_page import VisitsPage
from src.ui.pages.delegations_pages.delegation_dashboard_page import (
    DelegationDashboardPage,
)
from src.ui.pages.delegations_pages.delegation_details_page import DelegationDetailsPage
from src.ui.pages.e_services_page import EServicesPage
from src.ui.pages.individual_page import IndividualPage
from src.ui.pages.login_page import LoginPage
from src.ui.pages.spaces_page import AdminSpacesPage
from src.ui.pages.sso_auth_page import SSOAuthPage
from src.ui.pages.um_pages.main_page import MainPage
from src.ui.pages.visa_pages.increse_quota_page import IncreaseQuotaPage
from src.ui.pages.visa_pages.issue_visa import IssueVisaPage
from src.ui.pages.visa_pages.perm_work_visa_page import PermWorkVisaPage
from src.ui.pages.visa_pages.transitional_page import TransitionalPage
from src.ui.pages.visa_pages.visa_request_page import VisaRequestPage
from src.ui.pages.workspaces_page import WorkspacesPage
from src.ui.pages.wp_page import LoWorkPermitPage


class QiwaUiClient:
    # Pages
    login_page = LoginPage()
    sso_auth_page = SSOAuthPage()
    workspace_page = WorkspacesPage()
    dashboard_page = DashboardPage()
    e_services_page = EServicesPage()
    admin_page = AdminPage()
    appointment_page = AppointmentRequestPage()
    change_occupation_page = ChangeOccupationPage()
    requests_page = RequestsPage()
    individual_page = IndividualPage()
    visits_page = VisitsPage()
    business_page = BusinessPage()
    delegation_dashboard_page = DelegationDashboardPage()
    delegation_details_page = DelegationDetailsPage()
    admin_spaces_page = AdminSpacesPage()
    lo_work_permit_page = LoWorkPermitPage()
    main_page = MainPage()
    transitional = TransitionalPage()
    work_visa = PermWorkVisaPage()
    visa_request = VisaRequestPage()
    issue_visa = IssueVisaPage()
    increse_quota = IncreaseQuotaPage()
    labor_office_appointments_page = LaborOfficeAppointmentsPage()
    labor_office_appointments_create_page = LaborOfficeAppointmentsCreatePage()
    labor_office_appointments_create_confirmation_page = LaborOfficeCreateConfirmationPage()

    # Components
    header = Header()
    footer = Footer()
    feedback = FeedbackPopup()
    email_popup = EmailConfirmationPopup()

    @allure.step
    def login_as_user(self, login: str, password: str = UserInfo.PASSWORD) -> QiwaUiClient:
        self.login_page.open_login_page()
        (
            self.sso_auth_page.enter_user_id(login)
            .enter_password(password)
            .login()
            .enter_otp_code("0")
            .confirm_otp_code()
        )
        return self

    @allure.step
    def login_as_new_user(self, login: str, password: str = UserInfo.PASSWORD) -> QiwaUiClient:
        QiwaApi().sso.login_user(login, password)
        QiwaApi().sso.pass_account_security()
        self.login_as_user(login, password)
        self.feedback.close_feedback()
        return self

    @allure.step
    def login_as_admin(self) -> QiwaUiClient:
        self.login_as_user("1215113732")
        self.workspace_page.should_have_workspace_list_appear().select_admin_account()
        return self

    @allure.step
    def open_work_permits(self) -> QiwaUiClient:
        browser.open("https://working-permits.qiwa.tech/working-permits")
        return self

    @allure.step
    def open_dashboard(self) -> QiwaUiClient:
        browser.open("https://spa.qiwa.tech/en/company")
        return self

    @allure.step
    def should_not_have_error_message(self) -> QiwaUiClient:
        browser.element(".error-message").should(be.in_dom.and_(be.not_.visible))
        return self

    @allure.step
    def open_delegation_dashboard_page(self) -> QiwaUiClient:
        browser.open(config.qiwa_urls.delegation_service)
        return self

    @allure.step
    def open_delegation_details_page(self, delegation_id: int | str) -> QiwaUiClient:
        browser.open(f"{config.qiwa_urls.delegation_service}/delegation-details/{delegation_id}")
        return self

    @allure.step
    def open_visa_page(self):
        browser.open(config.qiwa_urls.visa_web_url)


qiwa = QiwaUiClient()
