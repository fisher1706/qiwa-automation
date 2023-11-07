from __future__ import annotations

from data.dedicated.employee_trasfer.employee_transfer_constants import type_4
from data.dedicated.models.contract_details import (
    ContractDetails,
    EmployeeDetails,
    EstablishmentDetails,
)
from data.dedicated.models.transfer_type import TransferType
from src.ui.pages.dedicated_pages.contract_management_page import ContractManagementPage


class ContractManagementActions(ContractManagementPage):
    def fill_establishment_details(self) -> ContractManagementActions:
        establishment_details = EstablishmentDetails()
        self.fill_field_role(establishment_details.role)
        self.fill_field_email(establishment_details.company_email)
        self.fill_field_work_location(establishment_details.work_location)
        return self

    def fill_employee_details(self) -> ContractManagementActions:
        employee_details = EmployeeDetails()
        contract_details = ContractDetails()

        self.select_dropdown_education_level(employee_details.education_level)
        self.fill_field_major(employee_details.major)
        self.fill_field_iban_number(contract_details.iban_number)
        self.fill_field_mobile_number(employee_details.mobile_number)
        self.fill_field_email(employee_details.email)
        return self

    def fill_contract_details(self, transfer_type: TransferType) -> ContractManagementActions:
        contract_details = ContractDetails()

        if transfer_type.code != type_4.code:
            self.fill_field_occupation(contract_details.occupation)
        self.fill_field_job_title_en(contract_details.job_title_en)
        self.fill_field_job_title_ar(contract_details.job_title_ar)
        self.fill_field_employee_number(contract_details.employee_number)
        self.fill_field_contract_period()
        self.fill_field_basic_salary(contract_details.basic_salary)
        return self
