from __future__ import annotations

from selene import be, command, have
from selene.support.shared.jquery_style import s, ss


class ContractManagementPage:
    otp_form = s("#otp-form")
    title_verification_code = otp_form.s("h2")
    field_verification_code = otp_form.ss("input")
    btn_verify = s("[form='otp-form']")

    btn_next_step = s("[type='submit']")

    dropdown = ss(".tippy-content li")
    field_work_location = s("#workLocation")
    dropdown_education_level = s("#education")
    field_major = s("#speciality")
    field_iban_number = s("#iban")
    field_mobile_number = s("#mobile")
    field_email = s("#email")

    # Contract details
    field_occupation = s("#Occupation")
    dropdown_occupation = s("")
    field_job_title_en = s("[name='jobTitle.en']")
    field_job_title_ar = s("[name='jobTitle.ar']")
    field_employee_number = s("#employeeNumber")
    radiobtn_contract_period_type = s("[data-component='RadioButton']")
    field_contract_period = s("#contractPeriod")
    field_start_date = s("[name='startDate.gregorian']")
    field_notice_period = s("#noticePeriod")
    field_trial_period = s("#trialPeriod")

    # Working time
    dropdown_contract_type = s("#contractTypeId")
    field_period = s("")

    dropdown_work_hours_type = s("")
    field_days_per_week = s("")
    field_daily_hours = s("")
    field_hours_per_week = s("")
    field_annual_vacations_days = s("")

    field_basic_salary = s("[name='financialObligations.basicSalary']")
    dropdown_salary_amount_type = s("")
    dropdown_salary_period = s("")

    field_housing_allowance = s("")
    dropdown_housing_allowance_type = s("")
    dropdown_housing_allowance_frequency = s("")

    field_transportation_allowance = s("")
    dropdown_transportation_allowance_type = s("")
    dropdown_transportation_allowance_frequency = s("")

    # Summary
    terms_checkbox = s("#terms + span")

    def wait_until_title_verification_code_appears(self, text: dict, locale: str):
        locator = self.title_verification_code
        locator.wait_until(be.visible)
        locator.should(have.exact_text(text[locale]))
        return self

    def proceed_2fa(self, otp_code: str = "0000"):
        for number, element in zip(otp_code, self.field_verification_code):
            element.perform(command.js.set_value("")).type(number)
        return self

    def click_btn_verify(self):
        self.btn_verify.click()
        return self

    def click_btn_next_step(self):
        self.btn_next_step.click()
        return self

    # Establishment Details
    def fill_field_work_location(self, data: str):
        self.field_work_location.perform(command.js.set_value("")).type(data)
        self.dropdown.element_by(have.text(data)).click()
        return self

    def select_dropdown_education_level(self, data: str):
        self.dropdown_education_level.click()
        self.dropdown.element_by(have.text(data)).click()
        return self

    def fill_field_major(self, data: str):
        self.field_major.perform(command.js.set_value("")).type(data)
        self.dropdown.element_by(have.text(data)).click()
        return self

    def fill_field_iban_number(self, data: str):
        self.field_iban_number.perform(command.js.set_value("")).type(data)
        return self

    def fill_field_mobile_number(self, data: str):
        self.field_mobile_number.perform(command.js.set_value("")).type(data)
        return self

    def fill_field_email(self, data: str):
        self.field_email.perform(command.js.set_value("")).type(data)
        return self

    # Contract Details
    def fill_field_occupation(self, data: str):
        self.field_occupation.should(be.visible).perform(command.js.set_value("")).type(data)
        self.dropdown_occupation.hover().click()
        return self

    def fill_field_job_title_en(self, data: str):
        self.field_job_title_en.perform(command.js.set_value("")).type(data)
        return self

    def fill_field_job_title_ar(self, data: str):
        self.field_job_title_ar.perform(command.js.set_value("")).type(data)
        return self

    def fill_field_employee_number(self, data: str):
        self.field_employee_number.hover().perform(command.js.set_value("")).type(data)
        return self

    def fill_field_contract_period(self):
        # TODO: Adjust method for different types of users
        # self.field_contract_period.should(be.visible).all("option").element_by(
        #     have.text(data)
        # ).click()
        self.radiobtn_contract_period_type.click()
        return self

    def fill_field_trial_period(self, data: str):
        self.field_trial_period.perform(command.js.set_value("")).type(data)
        return self

    def select_type_of_work(self, data: str):
        self.dropdown_contract_type.should(be.visible).all("option").element_by(
            have.text(data)
        ).click()
        return self

    def fill_field_period(self, data: str):
        self.field_period.perform(command.js.set_value("")).type(data)
        return self

    def fill_field_notice_period(self, data: str):
        self.field_notice_period.perform(command.js.set_value("")).type(data)
        return self

    def select_working_hours_type(self, data: str):
        self.dropdown_work_hours_type.should(be.visible).all("option").element_by(
            have.text(data)
        ).click()
        return self

    def fill_field_days_per_week(self, data: str):
        self.field_days_per_week.perform(command.js.set_value("")).type(data)
        return self

    def fill_field_daily_hours(self, data: str):
        self.field_daily_hours.perform(command.js.set_value("")).type(data)
        return self

    def fill_field_hours_per_week(self, data: str):
        self.field_hours_per_week.perform(command.js.set_value("")).type(data)
        return self

    def fill_field_annual_vacations_days(self, data: str):
        self.field_annual_vacations_days.perform(command.js.set_value("")).type(data)
        return self

    def fill_field_basic_salary(self, data: str):
        self.field_basic_salary.perform(command.js.set_value("")).type(data)
        return self

    def select_dropdown_salary_amount_type(self, data: str):
        self.dropdown_salary_amount_type.should(be.visible).all("option").element_by(
            have.text(data)
        ).click()
        return self

    def select_dropdown_salary_period(self, data: str):
        self.dropdown_salary_period.should(be.visible).all("option").element_by(
            have.text(data)
        ).click()
        return self

    def fill_field_housing_allowance(self, data: str):
        self.field_housing_allowance.perform(command.js.set_value("")).type(data)

    def select_dropdown_housing_allowance_type(self, data: str):
        self.dropdown_housing_allowance_type.should(be.visible).all("option").element_by(
            have.text(data)
        ).click()
        return self

    def select_dropdown_housing_allowance_frequency(self, data: str):
        self.dropdown_housing_allowance_frequency.should(be.visible).all("option").element_by(
            have.text(data)
        ).click()
        return self

    def fill_field_transportation_allowance(self, data: str):
        self.field_transportation_allowance.perform(command.js.set_value("")).type(data)
        return self

    def select_dropdown_transportation_allowance_type(self, data: str):
        self.dropdown_transportation_allowance_type.should(be.visible).all("option").element_by(
            have.text(data)
        ).click()
        return self

    def select_dropdown_transportation_allowance_frequency(self, data: str):
        self.dropdown_transportation_allowance_frequency.should(be.visible).all(
            "option"
        ).element_by(have.text(data)).click()
        return self

    # Summary
    def select_terms_checkbox(self) -> ContractManagementPage:
        self.terms_checkbox.hover().click()
        return self
