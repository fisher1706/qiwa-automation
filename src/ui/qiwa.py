from __future__ import annotations

import pytest
from selene import be, have
from selene.support.shared import browser

import config
from data.constants import Language, UserInfo
from src.ui.components.code_verification import CodeVerification
from src.ui.components.dedicated.email_confirmation_pop_up import EmailConfirmationPopup
from src.ui.components.delegation.localisation_change import (
    DelegationLocalisationChange,
)
from src.ui.components.delegation.resend_modal import ResendModal
from src.ui.components.delegation.revoke_modal import RevokeModal
from src.ui.components.delegation.toast_message import DelegationToast
from src.ui.components.feedback_pop_up import FeedbackPopup
from src.ui.components.footer import Footer
from src.ui.components.header import Header
from src.ui.components.meet_qiwa_popup import MeetQiwaPopup
from src.ui.components.payment_gateway import PaymentPage
from src.ui.pages.admin_page import AdminPage
from src.ui.pages.appointments.labor_office_appointment_edit import (
    LaborOfficeAppointmentsEditPage,
)
from src.ui.pages.appointments.labor_office_appointment_view import (
    LaborOfficeAppointmentsViewPage,
)
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
from src.ui.pages.dedicated_pages.contract_management_page import ContractManagementPage
from src.ui.pages.dedicated_pages.employee_transfer.employee_transfer_page import (
    EmployeeTransferPage,
)
from src.ui.pages.dedicated_pages.induviduals.my_resume_page import MyResumePage
from src.ui.pages.dedicated_pages.requests_page import RequestsPage
from src.ui.pages.dedicated_pages.visits_page import VisitsPage
from src.ui.pages.delegations_pages.add_new_delegation_page import AddDelegationPage
from src.ui.pages.delegations_pages.delegation_dashboard_page import (
    DelegationDashboardPage,
)
from src.ui.pages.delegations_pages.delegation_details_page import DelegationDetailsPage
from src.ui.pages.delegations_pages.partner_approval_page import PartnerApprovalPage
from src.ui.pages.delegations_pages.verify_delegation_letter_page import (
    VerifyDelegationLetterPage,
)
from src.ui.pages.e_services_page import EServicesPage
from src.ui.pages.employee_list_page import EmployeeListPage
from src.ui.pages.individual_page import IndividualPage
from src.ui.pages.lo_saudi_certificate_page import LoSaudiCertificatePage
from src.ui.pages.spaces_page import AdminSpacesPage
from src.ui.pages.sso_pages.add_birthday_page import AddBirthdayPage
from src.ui.pages.sso_pages.change_phone_number_page import ChangePhoneNumberPage
from src.ui.pages.sso_pages.login_page import LoginPage
from src.ui.pages.sso_pages.secure_account_page import SecureAccountPage
from src.ui.pages.user_management_pages.main_page import UserManagementMainPage
from src.ui.pages.violations_pages.violation_details_page import ViolationDetailsPage
from src.ui.pages.violations_pages.violations_page import ViolationsPage
from src.ui.pages.visa_pages.balance_request import BalanceRequest
from src.ui.pages.visa_pages.increse_quota_page import IncreaseQuotaPage
from src.ui.pages.visa_pages.issue_visa import IssueVisaPage
from src.ui.pages.visa_pages.perm_work_visa_page import PermWorkVisaPage
from src.ui.pages.visa_pages.transitional_page import TransitionalPage
from src.ui.pages.visa_pages.visa_request_page import VisaRequestPage
from src.ui.pages.workspaces_page import WorkspacesPage
from src.ui.pages.wp_page import LoWorkPermitPage
from utils.allure import allure_steps


@allure_steps
class QiwaUiClient:
    # Pages
    login_page = LoginPage()
    add_birth_day_page = AddBirthdayPage()
    change_phone_number_page = ChangePhoneNumberPage()
    secure_account_page = SecureAccountPage()
    workspace_page = WorkspacesPage()
    dashboard_page = DashboardPage()
    e_services_page = EServicesPage()
    admin_page = AdminPage()
    appointment_page = AppointmentRequestPage()
    change_occupation_page = ChangeOccupationPage()
    requests_page = RequestsPage()
    individual_page = IndividualPage()
    my_resume_page = MyResumePage()
    visits_page = VisitsPage()
    business_page = BusinessPage()
    delegation_dashboard_page = DelegationDashboardPage()
    delegation_details_page = DelegationDetailsPage()
    delegation_partner_approval_page = PartnerApprovalPage()
    delegation_letter_verify_page = VerifyDelegationLetterPage()
    add_delegation_page = AddDelegationPage()
    admin_spaces_page = AdminSpacesPage()
    lo_work_permit_page = LoWorkPermitPage()
    main_page = UserManagementMainPage()
    transitional = TransitionalPage()
    work_visa = PermWorkVisaPage()
    visa_request = VisaRequestPage()
    issue_visa = IssueVisaPage()
    increase_quota = IncreaseQuotaPage()
    balnce_request = BalanceRequest()
    labor_office_appointments_page = LaborOfficeAppointmentsPage()
    labor_office_appointments_view_page = LaborOfficeAppointmentsViewPage()
    labor_office_appointments_create_page = LaborOfficeAppointmentsCreatePage()
    labor_office_appointments_create_confirmation_page = LaborOfficeCreateConfirmationPage()
    labor_office_appointments_edit_page = LaborOfficeAppointmentsEditPage()
    employee_transfer_page = EmployeeTransferPage()
    employee_list_page = EmployeeListPage()
    contract_management_page = ContractManagementPage()
    lo_saudization_certificate_page = LoSaudiCertificatePage()
    violations_page = ViolationsPage()
    violation_details_page = ViolationDetailsPage()

    # Components
    header = Header()
    footer = Footer()
    feedback = FeedbackPopup()
    email_popup = EmailConfirmationPopup()
    meet_qiwa_popup = MeetQiwaPopup()
    resend_modal = ResendModal()
    revoke_modal = RevokeModal()
    toast_message = DelegationToast()
    delegation_localisation = DelegationLocalisationChange()
    code_verification = CodeVerification()

    def login_as_user(self, login: str, password: str = UserInfo.PASSWORD) -> QiwaUiClient:
        self.open_login_page()
        self.header.change_local(Language.EN)
        (self.login_page.enter_login(login).enter_password(password).click_login_button())
        (self.login_page.otp_pop_up.fill_in_code().click_confirm_button())
        return self

    def login_as_admin(self) -> QiwaUiClient:
        self.login_as_user("1215113732")
        self.workspace_page.should_have_workspace_list_appear().select_admin_account()
        return self

    def open_login_page(self) -> QiwaUiClient:
        browser.open(config.qiwa_urls.sso)
        return self

    def open_work_permits(self) -> QiwaUiClient:
        browser.open("https://working-permits.qiwa.tech/working-permits")
        return self

    def open_dashboard(self) -> QiwaUiClient:
        browser.open("https://spa.qiwa.tech/en/company")
        return self

    def should_not_have_error_message(self) -> QiwaUiClient:
        browser.element(".error-message").should(be.in_dom.and_(be.not_.visible))
        return self

    def open_delegation_dashboard_page(self) -> QiwaUiClient:
        browser.open(config.qiwa_urls.delegation_service)
        return self

    def open_delegation_details_page(self, delegation_id: int | str) -> QiwaUiClient:
        browser.open(f"{config.qiwa_urls.delegation_service}/delegation-details/{delegation_id}")
        return self

    def open_add_new_delegation_page(self) -> QiwaUiClient:
        browser.open(f"{config.qiwa_urls.delegation_service}/create-delegation")
        return self

    def open_verify_delegation_letter_page(self) -> QiwaUiClient:
        browser.open(f"{config.qiwa_urls.delegation_service}/verify")
        return self

    def open_visa_page(self) -> QiwaUiClient:
        browser.open(config.qiwa_urls.visa_web_url)
        for _ in range(3):
            browser.should(have.url_containing(config.qiwa_urls.visa_web_url))
            if browser.with_(timeout=3).matching(
                have.url_containing(config.qiwa_urls.visa_web_url)
            ):
                break
            browser.open(config.qiwa_urls.visa_web_url)
        else:
            pytest.fail(f"Could not reach to home page {config.qiwa_urls.visa_web_url}")
        return self

    def open_user_management_page(self) -> QiwaUiClient:
        browser.open(config.qiwa_urls.ui_user_management)
        return self

    def open_user_details_page(self, personal_number: int) -> QiwaUiClient:
        browser.open(f"{config.qiwa_urls.ui_user_management}/user-details/{personal_number}")
        return self

    def open_labor_office_appointments_page(self) -> QiwaUiClient:
        browser.open(config.qiwa_urls.appointment_booking)
        self.labor_office_appointments_page.wait_page_to_load()
        return self

    def open_labor_office_appointments_page_individual(self) -> QiwaUiClient:
        browser.open(config.qiwa_urls.appointment_booking_individual)
        self.individual_page.wait_page_to_load()
        return self

    def open_e_services_page(self) -> QiwaUiClient:
        browser.open(config.qiwa_urls.e_services)
        return self

    def open_employee_list_page(self) -> QiwaUiClient:
        browser.open(config.qiwa_urls.employee_list)
        return self


qiwa = QiwaUiClient()
