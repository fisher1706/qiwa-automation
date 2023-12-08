import time
from typing import Optional

from data.constants import EService, Language, UserInfo
from data.dedicated.contract_management.contract_management_constants import (
    CONTRACT_TYPE,
    TITLE,
    VERIFICATION_CODE,
    SuccessMessages,
)
from data.dedicated.employee_trasfer.employee_transfer_constants import type_4
from data.dedicated.models.contract_details import (
    ContractDetails,
    EmployeeDetails,
    EstablishmentDetails,
)
from data.dedicated.models.laborer import Laborer
from data.dedicated.models.transfer_type import TransferType
from data.dedicated.models.user import User
from src.ui.actions.e_services import EServiceActions
from src.ui.components.footer import Footer
from src.ui.pages.dedicated_pages.old_contract_management_page import (
    OldContractManagementPage,
)
from src.ui.pages.workspaces_page import WorkspacesPage
from src.ui.qiwa import qiwa


# pylint: disable=duplicate-code
class OldContractManagementActions(OldContractManagementPage):
    def __init__(self):
        super().__init__()
        self.workspace_actions = WorkspacesPage()
        self.e_services_action = EServiceActions()
        self.footer = Footer()

    def fill_establishment_details(self, transfer_type: TransferType):
        establishment_details = EstablishmentDetails()
        if transfer_type.code != type_4.code:
            self.fill_field_company_email(establishment_details.company_email)
            self.fill_field_role(establishment_details.role)
        self.fill_field_work_location(establishment_details.work_location)

    def fill_employee_details(self, transfer_type: TransferType, laborer: Laborer):
        employee_details = EmployeeDetails()
        if transfer_type.code != type_4.code:
            employee_details.passport_no = str(laborer.personal_number)
            employee_details.date_of_birth = laborer.birthdate
            self.fill_field_name(employee_details.name)
            self.select_dropdown_marital_status(employee_details.marital_status[1])
            self.select_dropdown_nationality(employee_details.nationality)
            self.fill_field_field_passport_no(employee_details.passport_no)
            self.fill_field_field_passport_expiry_date(employee_details.passport_expiry_date)
            self.fill_field_date_of_birth(employee_details.date_of_birth)
            self.fill_field_dropdown_gender(employee_details.gender)
            self.fill_field_dropdown_religion(employee_details.religion)
            self.select_checkbox_confirmation()

        self.select_dropdown_education_level(employee_details.education_level)
        self.fill_field_major(employee_details.major)
        self.fill_field_mobile_number(employee_details.mobile_number)
        self.fill_field_email(employee_details.email)

    def fill_contract_details(self, transfer_type: TransferType):
        contract_details = ContractDetails()
        if transfer_type.code != type_4.code:
            self.fill_field_occupation(contract_details.occupation)
        elif transfer_type.code != type_4.code:
            self.fill_field_occupation(contract_details.occupation)
            self.fill_field_iban_number(contract_details.iban_number)
        else:
            self.fill_field_iban_number(contract_details.iban_number)
        self.fill_field_job_title_en(contract_details.job_title_en)
        self.fill_field_job_title_ar(contract_details.job_title_ar)
        self.fill_field_employee_number(contract_details.employee_number)
        self.fill_field_contract_period(contract_details.contract_period[0])
        self.fill_field_basic_salary(contract_details.basic_salary)

    def fill_contract_info(
        self, laborer: Optional[Laborer] = None, transfer_type: TransferType = None
    ):
        self.fill_establishment_details(transfer_type)
        self.fill_employee_details(transfer_type, laborer)
        self.fill_contract_details(transfer_type)

    def navigate_to_cm_service(self, user: User):
        qiwa.login_as_user(user.personal_number, UserInfo.PASSWORD)
        self.workspace_actions.select_company_account_with_sequence_number(user.sequence_number)
        self.footer.click_on_lang_button(Language.EN)
        self.e_services_action.select_e_service(e_service_name=EService.CONTRACT_MANAGEMENT)
        self.wait_until_title_verification_code_appears(VERIFICATION_CODE, Language.EN)
        self.proceed_2fa().click_btn_verify()
        self.verify_title(TITLE, Language.EN)

    def find_employee(self, laborer: Laborer):
        for _ in range(5):
            self.fill_national_iqama_id(str(laborer.personal_number))
            self.fill_date(laborer.birthdate)
            self.click_btn_find()
            if self.verify_employee_id(str(laborer.personal_number)):
                break
            time.sleep(1)

    def create_template(self):
        self.click_btn_create_template()
        self.verify_title_contract_type(CONTRACT_TYPE, Language.EN)
        self.fill_field_template_name()
        self.fill_field_description()
        self.click_btn_next()
        employee_details = EmployeeDetails()
        contract_details = ContractDetails()
        self.fill_field_company_email(employee_details.email)
        self.fill_field_contract_period(contract_details.contract_period[0])
        self.fill_field_notice_period(contract_details.notice_period)
        self.click_btn_next()
        self.click_btn_save_template()
        self.verify_success_template_creation(
            SuccessMessages.MSG_SUCCESS_TEMPLATE_CREATION, Language.EN
        )
