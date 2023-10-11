from data.constants import UserType
from data.dedicated.contract_details import (
    ContractDetails,
    EmployeeDetails,
    EstablishmentDetails,
)
from src.ui.pages.dedicated_pages.contract_management_page import ContractManagementPage


class ContractManagementActions(ContractManagementPage):
    def fill_establishment_details(self):
        establishment_details = EstablishmentDetails()
        self.fill_field_work_location(establishment_details.work_location)
        return self

    def fill_employee_details(self):
        employee_details = EmployeeDetails()
        contract_details = ContractDetails()

        self.select_dropdown_education_level(employee_details.education_level)
        self.fill_field_major(employee_details.major)
        self.fill_field_iban_number(contract_details.iban_number)
        self.fill_field_mobile_number(employee_details.mobile_number)
        self.fill_field_email(employee_details.email)
        return self

    def fill_contract_details(self, user_type: UserType = None):
        contract_details = ContractDetails()

        if user_type == UserType.EXPAT:
            self.fill_field_occupation(contract_details.occupation)
        elif user_type == UserType.USER:
            self.fill_field_occupation(contract_details.occupation)
            self.fill_field_iban_number(contract_details.iban_number)
        self.fill_field_job_title_en(contract_details.job_title_en)
        self.fill_field_job_title_ar(contract_details.job_title_ar)
        self.fill_field_employee_number(contract_details.employee_number)
        self.fill_field_contract_period(contract_details.contract_period[0])
        self.fill_field_basic_salary(contract_details.basic_salary)
        return self
