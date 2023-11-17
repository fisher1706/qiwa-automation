from __future__ import annotations

import allure

from data.dedicated.employee_trasfer.employee_transfer_constants import type_4
from data.dedicated.models.contract_details import (
    ContractDetails,
    EmployeeDetails,
    EstablishmentDetails,
)
from data.dedicated.models.laborer import Laborer
from data.dedicated.models.transfer_type import TransferType
from src.ui.qiwa import qiwa
from utils.allure import allure_steps


@allure_steps
class ContractManagementActions:
    def fill_establishment_details(self) -> ContractManagementActions:
        establishment_details = EstablishmentDetails()
        qiwa.contract_management_page.fill_field_role(establishment_details.role)
        qiwa.contract_management_page.fill_field_email(establishment_details.company_email)
        qiwa.contract_management_page.fill_field_work_location(establishment_details.work_location)
        return self

    def fill_employee_details(self) -> ContractManagementActions:
        employee_details = EmployeeDetails()
        contract_details = ContractDetails()

        qiwa.contract_management_page.select_dropdown_education_level(
            employee_details.education_level
        )
        qiwa.contract_management_page.fill_field_major(employee_details.major)
        qiwa.contract_management_page.fill_field_iban_number(contract_details.iban_number)
        qiwa.contract_management_page.fill_field_mobile_number(employee_details.mobile_number)
        qiwa.contract_management_page.fill_field_email(employee_details.email)
        return self

    def fill_contract_details(self, transfer_type: TransferType) -> ContractManagementActions:
        contract_details = ContractDetails()

        if transfer_type.code != type_4.code:
            qiwa.contract_management_page.fill_field_occupation(contract_details.occupation)
        qiwa.contract_management_page.fill_field_job_title_en(contract_details.job_title_en)
        qiwa.contract_management_page.fill_field_job_title_ar(contract_details.job_title_ar)
        qiwa.contract_management_page.fill_field_employee_number(contract_details.employee_number)
        qiwa.contract_management_page.fill_field_contract_period()
        qiwa.contract_management_page.fill_field_basic_salary(contract_details.basic_salary)
        return self

    def create_contract(self, laborer: Laborer):
        qiwa.contract_management_page.click_btn_next_step()
        self.fill_establishment_details()
        qiwa.contract_management_page.click_btn_next_step()
        self.fill_employee_details()
        qiwa.contract_management_page.click_btn_next_step()
        self.fill_contract_details(laborer.transfer_type)
        qiwa.contract_management_page.click_btn_next_step().select_terms_checkbox().click_btn_next_step()


contract_management_actions = ContractManagementActions()
