import allure
import pytest

from data.constants import ContractManagement, Language
from data.dedicated.contract_details import ContractDetails, EmployeeDetails
from data.dedicated.contract_management import employer
from src.ui.actions.old_contract_management import OldContractManagementActions


@allure.feature('Contract Management Templates')
@pytest.mark.skip("Old design")
class TestContractManagementTemplates:  # pylint: disable=unused-argument, too-many-statements

    @pytest.fixture(autouse=True)
    def pre_test(self):
        self.contract_management_actions = OldContractManagementActions()

    @allure.title('Creating a template with only required fields')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1221&case_id=10999')
    def test_creating_a_template_with_only_required_fields(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.click_btn_contract_templates()
        self.contract_management_actions.create_template()

    @allure.title('Creating a template in Arabic&English, Specified Period with daily working hours type (normal flow)')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1221&case_id=10999')
    def test_creating_a_template_in_arabic_english_specified_period_with_daily_working_hours_type(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.click_btn_contract_templates()
        self.contract_management_actions.click_btn_create_template()
        self.contract_management_actions.verify_title_contract_type(ContractManagement.CONTRACT_TYPE, Language.EN)
        self.contract_management_actions.fill_field_template_name()
        self.contract_management_actions.fill_field_description()
        self.contract_management_actions.click_btn_next()
        employee_details = EmployeeDetails()
        contract_details = ContractDetails()
        self.contract_management_actions.fill_field_company_email(employee_details.email)

        self.contract_management_actions.fill_field_job_title_en(contract_details.job_title_en)
        self.contract_management_actions.fill_field_job_title_ar(contract_details.job_title_ar)
        self.contract_management_actions.fill_field_contract_period(contract_details.contract_period[0])
        self.contract_management_actions.fill_field_period(contract_details.period)
        self.contract_management_actions.fill_field_notice_period(contract_details.notice_period)
        self.contract_management_actions.fill_field_trial_period(contract_details.trial_period)
        self.contract_management_actions.select_working_hours_type(contract_details.working_hours_type[0])

        self.contract_management_actions.fill_field_days_per_week(contract_details.days_per_week)
        self.contract_management_actions.fill_field_daily_hours(contract_details.daily_hours)
        self.contract_management_actions.fill_field_annual_vacations_days(contract_details.annual_vacations_days)

        self.contract_management_actions.fill_field_basic_salary(contract_details.basic_salary)
        self.contract_management_actions.select_dropdown_salary_amount_type(contract_details.type_for_basic_salary)
        self.contract_management_actions.select_dropdown_salary_period(contract_details.frequency_for_basic_salary)

        self.contract_management_actions.fill_field_housing_allowance(contract_details.housing_allowance)
        self.contract_management_actions.select_dropdown_housing_allowance_type(
            contract_details.type_for_housing_allowance)
        self.contract_management_actions.select_dropdown_housing_allowance_frequency(
            contract_details.frequency_for_housing_allowance)

        self.contract_management_actions.fill_field_transportation_allowance(contract_details.transportation_allowance)
        self.contract_management_actions.select_dropdown_transportation_allowance_type(
            contract_details.type_for_transportation_allowance)
        self.contract_management_actions.select_dropdown_transportation_allowance_frequency(
            contract_details.frequency_for_transportation_allowance)

        self.contract_management_actions.click_btn_add_financial_benefits()
        self.contract_management_actions.fill_field_benefit_name_en(contract_details.financial_benefits.name_english)
        self.contract_management_actions.fill_field_benefit_name_an(contract_details.financial_benefits.name_arabic)
        self.contract_management_actions.fill_field_amount(contract_details.financial_benefits.amount)
        self.contract_management_actions.select_dropdown_benefit_type(contract_details.financial_benefits.benefit_type)
        self.contract_management_actions.select_dropdown_benefit_frequency(
            contract_details.financial_benefits.frequency_for_financial_benefits)

        self.contract_management_actions.click_btn_add_additional_clauses()
        self.contract_management_actions.select_checkboxes_article()
        self.contract_management_actions.click_btn_modal_add_additional_clauses()

        self.contract_management_actions.fill_field_non_compete_agreement_period(
            contract_details.additional_clauses.non_compete_agreement_period)
        self.contract_management_actions.fill_field_non_compete_agreement_field(
            contract_details.additional_clauses.non_compete_agreement_field)
        self.contract_management_actions.fill_field_non_compete_agreement_location(
            contract_details.additional_clauses.non_compete_agreement_location)
        self.contract_management_actions.fill_field_non_disclosure_clause_period(
            contract_details.additional_clauses.non_disclosure_clause_period)
        self.contract_management_actions.fill_field_non_disclosure_clause_field(
            contract_details.additional_clauses.non_disclosure_clause_field)
        self.contract_management_actions.fill_field_non_disclosure_clause_location(
            contract_details.additional_clauses.non_disclosure_clause_location)
        self.contract_management_actions.fill_field_amount_from_1st_party_to_2nd_party(
            contract_details.additional_clauses.amount_from_1st_party_to_2nd_party)
        self.contract_management_actions.fill_field_amount_from_2nd_party_to_1st_party(
            contract_details.additional_clauses.amount_from_2nd_party_to_1st_party)

        self.contract_management_actions.click_btn_add_additional_terms()
        self.contract_management_actions.click_btn_modal_add_additional_terms()
        self.contract_management_actions.fill_field_english_term(contract_details.additional_terms.additional_terms_en)
        self.contract_management_actions.fill_field_arabic_term(contract_details.additional_terms.additional_terms_ar)
        self.contract_management_actions.click_btn_add_term()
        self.contract_management_actions.click_btn_save_and_close()

        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.click_btn_save_template()
        self.contract_management_actions.verify_success_template_creation(
            ContractManagement.MSG_SUCCESS_TEMPLATE_CREATION,
            Language.EN
        )

    @allure.title('Creating a template in Arabic, Non-Specified Period with weekly working hours type (normal flow)')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1221&case_id=11006')
    def test_creating_a_template_in_arabic_non_specified_period_with_weekly_working_hours_type(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.click_btn_contract_templates()
        self.contract_management_actions.click_btn_create_template()
        self.contract_management_actions.verify_title_contract_type(ContractManagement.CONTRACT_TYPE, Language.EN)
        self.contract_management_actions.fill_field_template_name()
        self.contract_management_actions.fill_field_description()
        self.contract_management_actions.select_arabic_only()
        self.contract_management_actions.click_btn_next()
        employee_details = EmployeeDetails()
        contract_details = ContractDetails()
        self.contract_management_actions.fill_field_company_email(employee_details.email)

        self.contract_management_actions.fill_field_job_title_ar(contract_details.job_title_ar)
        self.contract_management_actions.fill_field_contract_period(contract_details.contract_period[1])
        self.contract_management_actions.fill_field_notice_period(contract_details.notice_period)
        self.contract_management_actions.fill_field_trial_period(contract_details.trial_period)

        self.contract_management_actions.select_working_hours_type(contract_details.working_hours_type[1])
        self.contract_management_actions.fill_field_hours_per_week(contract_details.hours_per_week)
        self.contract_management_actions.fill_field_annual_vacations_days(contract_details.annual_vacations_days)

        self.contract_management_actions.fill_field_basic_salary(contract_details.basic_salary)
        self.contract_management_actions.select_dropdown_salary_amount_type(contract_details.type_for_basic_salary)
        self.contract_management_actions.select_dropdown_salary_period(contract_details.frequency_for_basic_salary)

        self.contract_management_actions.fill_field_housing_allowance(contract_details.housing_allowance)
        self.contract_management_actions.select_dropdown_housing_allowance_type(
            contract_details.type_for_housing_allowance)
        self.contract_management_actions.select_dropdown_housing_allowance_frequency(
            contract_details.frequency_for_housing_allowance)

        self.contract_management_actions.fill_field_transportation_allowance(contract_details.transportation_allowance)
        self.contract_management_actions.select_dropdown_transportation_allowance_type(
            contract_details.type_for_transportation_allowance)
        self.contract_management_actions.select_dropdown_transportation_allowance_frequency(
            contract_details.frequency_for_transportation_allowance)

        self.contract_management_actions.click_btn_add_financial_benefits()
        self.contract_management_actions.fill_field_benefit_name_an(contract_details.financial_benefits.name_arabic)
        self.contract_management_actions.fill_field_amount(contract_details.financial_benefits.amount)
        self.contract_management_actions.select_dropdown_benefit_type(contract_details.financial_benefits.benefit_type)
        self.contract_management_actions.select_dropdown_benefit_frequency(
            contract_details.financial_benefits.frequency_for_financial_benefits)

        self.contract_management_actions.click_btn_add_additional_clauses()
        self.contract_management_actions.select_checkboxes_article()
        self.contract_management_actions.click_btn_modal_add_additional_clauses()

        self.contract_management_actions.fill_field_non_compete_agreement_period(
            contract_details.additional_clauses.non_compete_agreement_period)
        self.contract_management_actions.fill_field_non_compete_agreement_field(
            contract_details.additional_clauses.non_compete_agreement_field)
        self.contract_management_actions.fill_field_non_compete_agreement_location(
            contract_details.additional_clauses.non_compete_agreement_location)
        self.contract_management_actions.fill_field_non_disclosure_clause_period(
            contract_details.additional_clauses.non_disclosure_clause_period)
        self.contract_management_actions.fill_field_non_disclosure_clause_field(
            contract_details.additional_clauses.non_disclosure_clause_field)
        self.contract_management_actions.fill_field_non_disclosure_clause_location(
            contract_details.additional_clauses.non_disclosure_clause_location)
        self.contract_management_actions.fill_field_amount_from_1st_party_to_2nd_party(
            contract_details.additional_clauses.amount_from_1st_party_to_2nd_party)
        self.contract_management_actions.fill_field_amount_from_2nd_party_to_1st_party(
            contract_details.additional_clauses.amount_from_2nd_party_to_1st_party)

        self.contract_management_actions.click_btn_add_additional_terms()
        self.contract_management_actions.click_btn_modal_add_additional_terms()
        self.contract_management_actions.fill_field_arabic_term(contract_details.additional_terms.additional_terms_ar)
        self.contract_management_actions.click_btn_add_term()
        self.contract_management_actions.click_btn_save_and_close()

        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.click_btn_save_template()
        self.contract_management_actions.verify_success_template_creation(
            ContractManagement.MSG_SUCCESS_TEMPLATE_CREATION,
            Language.EN
        )

    @allure.title('Creating a template during creating a contract')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1221&case_id=11007')
    def test_creating_a_template_during_creating_a_contract(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.click_btn_create_contract()
        self.contract_management_actions.click_link_manage_templates()
        self.contract_management_actions.create_template()

    @allure.title('Updating a template from template details page')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1221&case_id=11008')
    def test_updating_a_template_from_template_details_page(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.click_btn_contract_templates()
        self.contract_management_actions.create_template()
        self.contract_management_actions.navigate_to_contract_templates_by_link()
        self.contract_management_actions.view_template()
        template_name = self.contract_management_actions.template_name
        self.contract_management_actions.verify_template_name(template_name)
        self.contract_management_actions.click_btn_modify()
        self.contract_management_actions.fill_field_template_name(' modified')
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.fill_field_job_title_en('modified')
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.click_btn_save_template()
        self.contract_management_actions.view_template()
        self.contract_management_actions.verify_template_name(template_name + ' modified')

    @allure.title('Updating a template from list of templates view')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1221&case_id=11009')
    def test_updating_a_template_from_list_of_templates_view(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.click_btn_contract_templates()
        self.contract_management_actions.create_template()
        self.contract_management_actions.navigate_to_contract_templates_by_link()
        self.contract_management_actions.edit_template()
        template_name = self.contract_management_actions.template_name
        self.contract_management_actions.fill_field_template_name(' modified')
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.fill_field_job_title_en('modified')
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.click_btn_save_template()
        self.contract_management_actions.view_template()
        self.contract_management_actions.verify_template_name(template_name + ' modified')

    @allure.title('Removing a template from template details page')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1221&case_id=11010')
    def test_removing_a_template_from_template_details_page(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.click_btn_contract_templates()
        self.contract_management_actions.create_template()
        self.contract_management_actions.navigate_to_contract_templates_by_link()
        self.contract_management_actions.view_template()
        template_name = self.contract_management_actions.template_name
        self.contract_management_actions.verify_template_name(template_name)
        self.contract_management_actions.click_btn_delete_template()
        self.contract_management_actions.click_btn_modal_delete_template()
        self.contract_management_actions.verify_successfully_removing_template()

    @allure.title('Removing a template from list of templates view')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1221&case_id=11011')
    def test_removing_a_template_from_list_of_templates_view(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.click_btn_contract_templates()
        self.contract_management_actions.create_template()
        self.contract_management_actions.navigate_to_contract_templates_by_link()
        self.contract_management_actions.remove_template()
        self.contract_management_actions.click_btn_modal_delete_template()
        self.contract_management_actions.verify_successfully_removing_template()
