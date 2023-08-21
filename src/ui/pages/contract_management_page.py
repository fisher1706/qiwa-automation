import time

from selene import be, browser, command, have, query
from selene.support.shared.jquery_style import s, ss

import config
from data.constants import ContractManagement, Language
from utils.random_manager import RandomManager
from src.ui.components.raw.table import Table


class ContractManagementPage:
    TITLE_VERIFICATION_CODE = ".otp-verification--title"
    FIELD_VERIFICATION_CODE = "input[name=otp]"
    BTN_VERIFY = '//button[.="Verify"]'

    BUTTONS = ss(".action-link")

    # Dashboard
    TITLE = ".dashboard-actions--box-title"
    DESCRIPTION = ".dashboard-actions--box-text"
    BLOCKS = ss(".contract-auth-indicator")
    CONTRACT_AUTHENTICATION = {
        ContractManagement.CONTRACT_AUTHENTICATION_SCORE_FOR_SAUDI_EMPLOYEES[
            Language.EN
        ]: BLOCKS.first,
        ContractManagement.CONTRACT_AUTHENTICATION_SCORE_FOR_EXPATS_EMPLOYEES[
            Language.EN
        ]: BLOCKS.second,
        ContractManagement.TOTAL_CONTRACT_AUTHENTICATION[Language.EN]: BLOCKS[2],
    }
    CONTRACT_AUTH_INFO = ".contract-auth-indicator--info"
    SCORE = ".score--without-label"
    BTN_CONTRACT_TEMPLATES = BUTTONS.first
    BTN_CREATE_BULK_CONTRACTS = BUTTONS.second
    BTN_CREATE_CONTRACT = BUTTONS[2]
    EMPLOY_STATUS = ss(".contract-type-selection-box")
    BTN_INSIDE_SAUDI_ARABIA = EMPLOY_STATUS.first
    BTN_OUTSIDE_SAUDI_ARABIA = EMPLOY_STATUS.second
    LINK_MANAGE_TEMPLATES = ".contract-type-selection--action"

    # Templates
    BTN_BACK_TO_CONTRACT_LIST = BUTTONS.first
    BTN_CREATE_TEMPLATE = BUTTONS.second
    NAVIGATE_BUTTONS = ss(".stepper-nav--primary button")
    BTN_BACK = NAVIGATE_BUTTONS.first
    BTN_SAVE_TEMPLATE = NAVIGATE_BUTTONS.second
    TITLE_CONTRACT_TYPE = ".create-template--header"
    FIELD_TEMPLATE_NAME = '[name="name"]'
    FIELD_DESCRIPTION = '[name="description"]'
    CONTRACT_TYPE = ss(".contract-type-selection-box--title")
    ARABIC_AND_ENGLISH = CONTRACT_TYPE.first
    ARABIC_ONLY = CONTRACT_TYPE.second

    # Contracts
    BTN_NEXT = '//button[.="Next"]'
    BTN_SUBMIT = '//button[.="Submit"]'
    CHECKBOX_AGREE = ".check"
    BTN_ADD_CONTRACT = '//span[.="Add contract"]'

    FIELD_IQAMA_ID = ".find-employee--number input"
    FIELD_DATE = '[name="date"]'
    BTN_FIND = ".grid-row.btn button"
    NATIONAL_ID = ss(".details-form .static-field")[3]

    FIELD_COMPANY_EMAIL = '[name="company-email"]'
    FIELD_ROLE = '[name="role"]'
    FIELD_WORK_LOCATION = ".textarea"
    DROPDOWN_WORK_LOCATION = ".autocomplete-input .dropdown-content"

    FIELD_NAME = '[name="employeeName"]'
    DROPDOWN_MARITAL_STATUS = '[name="maritalStatus"]'
    DROPDOWN_NATIONALITY = '[name="nationality"]'
    FIELD_PASSPORT_NO = '[name="passportNumber"]'
    FIELD_PASSPORT_EXPIRY_DATE = '[name="expiryDate"]'
    FIELD_DATE_OF_BIRTH = '[name="dateOfBirth"]'
    DROPDOWN_GENDER = '[name="gender"]'
    DROPDOWN_RELIGION = '[name="religion"]'
    CHECKBOX_CONFIRMATION = '[name="isPersonalDataConfirmed"] + span'

    DROPDOWN_EDUCATION_LEVEL = '[name="education"]'
    FIELD_MAJOR = '[name="speciality"]'
    FIELD_MOBILE_NUMBER = '[type="tel"]'
    FIELD_EMAIL = '[name="email"]'

    FIELD_OCCUPATION = '[name="occupation"]'
    DROPDOWN_OCCUPATION = '[label="Occupation"] .dropdown-item span'
    FIELD_JOB_TITLE_EN = '[name="jobTitleEn"]'
    FIELD_JOB_TITLE_AR = '[name="jobTitleAr"]'
    FIELD_EMPLOYEE_NUMBER = '[name="employeeNumber"]'
    FIELD_CONTRACT_PERIOD = '[name="contractDurationId"]'
    DROPDOWN_CONTRACT_TYPE = '[name="contractTypeId"]'
    DROPDOWN_WORK_HOURS_TYPE = '[name="workHoursType"]'
    FIELD_TRIAL_PERIOD = '[name="trialPeriod"]'
    FIELD_PERIOD = '[name="contractPeriod"]'
    FIELD_NOTICE_PERIOD = '[name="noticePeriod"]'

    DROPDOWN_WORKING_HOURS_TYPE = '[name="workHoursType"]'
    FIELD_DAYS_PER_WEEK = '[name="workHoursType"]'
    FIELD_DAILY_HOURS = '[name="workHoursType"]'
    FIELD_HOURS_PER_WEEK = '[name="hoursPerWeek"]'
    FIELD_ANNUAL_VACATIONS_DAYS = '[name="annualVacationDays"]'

    FIELD_BASIC_SALARY = '[name="basicSalary"]'
    DROPDOWN_SALARY_AMOUNT_TYPE = '[name="salaryAmountType"]'
    DROPDOWN_SALARY_PERIOD = '[name="salaryPeriod"]'

    FIELD_HOUSING_ALLOWANCE = '[name="housingAllowance-amount"]'
    DROPDOWN_HOUSING_ALLOWANCE_TYPE = '[name="housingAllowance-type"]'
    DROPDOWN_HOUSING_ALLOWANCE_FREQUENCY = '[name="housingAllowance-frequency"]'

    FIELD_TRANSPORTATION_ALLOWANCE = '[name="transportationAllowance-amount"]'
    DROPDOWN_TRANSPORTATION_ALLOWANCE_TYPE = '[name="transportationAllowance-type"]'
    DROPDOWN_TRANSPORTATION_ALLOWANCE_FREQUENCY = '[name="transportationAllowance-frequency"]'

    # Financial Benefits
    BTN_ADD_FINANCIAL_BENEFITS = ".other-benefits button"
    FIELD_BENEFIT_NAME_EN = '[name="benefit-name-en-0"]'
    FIELD_BENEFIT_NAME_AR = '[name="benefit-name-ar-0"]'
    FIELD_AMOUNT = '[name="benefit-amount-0"]'
    DROPDOWN_BENEFIT_TYPE = '[name="benefit-type-0"]'
    DROPDOWN_BENEFIT_FREQUENCY = '[name="benefit-frequency-0"]'

    # Additional Clauses
    BTN_ADD_ADDITIONAL_CLAUSES = ".optional-articles button"
    CHECKBOXES_ARTICLE = ".optional-articles-modal .checkbox"
    BTN_MODAL_ADD_ADDITIONAL_CLAUSES = ".optional-articles-modal--btn"

    FIELD_NON_COMPETE_AGREEMENT_PERIOD = '[name="nonCompeteData.period"]'
    FIELD_NON_COMPETE_AGREEMENT_FIELD = '[name="nonCompeteData.field"]'
    FIELD_NON_COMPETE_AGREEMENT_LOCATION = '[name="nonCompeteData.location"]'
    FIELD_NON_DISCLOSURE_CLAUSE_PERIOD = '[name="nonDisclosureClause.period"]'
    FIELD_NON_DISCLOSURE_CLAUSE_FIELD = '[name="nonDisclosureClause.field"]'
    FIELD_NON_DISCLOSURE_CLAUSE_LOCATION = '[name="nonDisclosureClause.location"]'
    FIELD_AMOUNT_FROM_1ST_PARTY_TO_2ND_PARTY = '[name="compensationAmount.firstParty"]'
    FIELD_AMOUNT_FROM_2ND_PARTY_TO_1ST_PARTY = '[name="compensationAmount.secondParty"]'

    # Additional Terms
    BTN_ADD_ADDITIONAL_TERMS = ".additional-terms-summary + div button"
    BTN_MODAL_ADD_ADDITIONAL_TERMS = ".additional-terms-modal--actions button"
    FIELD_ENGLISH_TERM = '[name="englishTerm"]'
    FIELD_ARABIC_TERM = '[name="arabicTerm"]'
    FORM_ACTIONS = ss(".additional-terms-form--actions button")
    BTN_REMOVE_TERM = FORM_ACTIONS.first
    BTN_ADD_TERM = FORM_ACTIONS.second
    BTN_SAVE_AND_CLOSE = ".additional-terms-modal--save-btn button"

    FIELD_IBAN_NUMBER = 'input[name="iban"]'
    LABORER_ID = '//div[.="ID"]/following-sibling::div'

    MSG_SUCCESS_CONTRACT = "h1.contract-sent-successfully--title"
    MSG_SUCCESS_TEMPLATE = "h1.contract-template-sent-successfully--title"

    BUTTONS_CONTAINER = ss(".button-container a")
    BTN_REVIEW_CREATE_CONTRACT = BUTTONS_CONTAINER.first
    BTN_REVIEW_VIEW_TEMPLATE = BUTTONS_CONTAINER.second
    BTN_REVIEW_CREATE_BULK_CONTRACTS = BUTTONS_CONTAINER[2]

    # CONTRACT TEMPLATES LIST
    TABLE = Table(s(".table"))
    TEMPLATES_TABLE_ACTION = ".templates-table--action"

    ACTIONS = ss(".contract-template--status button")
    BTN_DELETE_TEMPLATE = ACTIONS.first
    BTN_MODIFY = ACTIONS.second

    BTN_MODAL_DELETE_TEMPLATE = ".confirmation-modal--btn"

    TOAST = ".toast"

    TEMPLATE_NAME = ".contract-template--name"

    def __init__(self):
        self.template_name = None
        self.cm_url = config.settings.contract_management
        self.templates_url = self.cm_url + "/templates"
        self.random_manager = RandomManager()

    def navigate_to_contract_management_by_link(self):
        browser.open(self.cm_url)

    def navigate_to_contract_templates_by_link(self):
        browser.open(self.templates_url)

    def wait_until_title_verification_code_appears(self, text: dict, locale: str):
        locator = s(self.TITLE_VERIFICATION_CODE)
        locator.wait_until(be.visible)
        locator.should(have.exact_text(text[locale]))

    def proceed_2fa(self, otp_code: str = "0000"):
        s(self.FIELD_VERIFICATION_CODE).perform(command.js.set_value("")).type(otp_code)
        return self

    def click_btn_verify(self):
        s(self.BTN_VERIFY).click()
        return self

    def click_btn_next(self):
        s(self.BTN_NEXT).should(be.clickable).s("span").click()
        return self

    # Dashboard
    def verify_title(self, text: dict, locale: str):
        s(self.TITLE).should(have.exact_text(text[locale]))

    def verify_description(self, text: dict, locale: str):
        s(self.DESCRIPTION).should(have.exact_text(text[locale]))

    def verify_score(self, name: dict, locale: str):
        self.CONTRACT_AUTHENTICATION[name[Language.EN]].s("h4").should(
            have.exact_text(name[locale])
        )

        authenticated_contracts = (
            self.CONTRACT_AUTHENTICATION[name[Language.EN]]
            .s(self.CONTRACT_AUTH_INFO)
            .ss("p")
            .first
        )
        unauthenticated_contracts = (
            self.CONTRACT_AUTHENTICATION[name[Language.EN]]
            .s(self.CONTRACT_AUTH_INFO)
            .ss("p")
            .second
        )

        authenticated_contracts.should(
            have.text(ContractManagement.AUTHENTICATED_CONTRACTS[locale])
        )
        unauthenticated_contracts.should(
            have.text(ContractManagement.UNAUTHENTICATED_CONTRACTS[locale])
        )

        score_authenticated_contracts = int(authenticated_contracts.get(query.text).split()[0])
        score_unauthenticated_contracts = int(unauthenticated_contracts.get(query.text).split()[0])
        score = str(int(score_authenticated_contracts / score_unauthenticated_contracts))
        self.CONTRACT_AUTHENTICATION[name[Language.EN]].s(self.SCORE).should(have.text(score))

    def verify_btn_contract_templates_is_clickable(self):
        self.BTN_CONTRACT_TEMPLATES.should(be.clickable)

    def verify_btn_create_bulk_contracts_is_clickable(self):
        self.BTN_CREATE_BULK_CONTRACTS.should(be.clickable)

    def verify_btn_create_contract_is_clickable(self):
        self.BTN_CREATE_CONTRACT.should(be.clickable)

    def click_btn_contract_templates(self):
        self.BTN_CONTRACT_TEMPLATES.click()

    def click_btn_create_bulk_contracts(self):
        self.BTN_CREATE_BULK_CONTRACTS.click()

    def click_btn_create_contract(self):
        self.BTN_CREATE_CONTRACT.click()

    def select_outside_saudi_arabia(self):
        self.BTN_OUTSIDE_SAUDI_ARABIA.click()

    def click_link_manage_templates(self):
        s(self.LINK_MANAGE_TEMPLATES).click()

    # Templates
    def click_btn_create_template(self):
        self.BTN_CREATE_TEMPLATE.click()

    def verify_title_contract_type(self, text: dict, locale: str):
        s(self.TITLE_CONTRACT_TYPE).should(have.exact_text(text[locale]))

    def fill_field_template_name(self, data: str = ""):
        template_name = (
            data if data else "Template Name " + self.random_manager.random_alphanumeric(5)
        )
        self.template_name = template_name
        s(self.FIELD_TEMPLATE_NAME).perform(command.js.set_value("")).type(template_name)

    def fill_field_description(self, data: str = "Description"):
        s(self.FIELD_DESCRIPTION).perform(command.js.set_value("")).type(data)

    def select_arabic_only(self):
        self.ARABIC_ONLY.click()

    def click_btn_save_template(self):
        self.BTN_SAVE_TEMPLATE.click()

    def verify_success_template_creation(self, data: str, locale: str):
        s(self.MSG_SUCCESS_TEMPLATE).should(have.exact_text(data[locale]))

    # Contracts
    def click_btn_submit(self):
        s(self.BTN_SUBMIT).click()

    def click_agree_checkbox(self):
        s(self.CHECKBOX_AGREE).perform(command.js.scroll_into_view).click()

    def click_btn_add_contract(self):
        s(self.BTN_ADD_CONTRACT).click()

    def fill_national_iqama_id(self, data: str):
        s(self.FIELD_IQAMA_ID).perform(command.js.set_value("")).type(data)

    def fill_date(self, data: str):
        s(self.FIELD_DATE).perform(command.js.set_value("")).type(data)

    def click_btn_find(self):
        s(self.BTN_FIND).should(be.clickable).click()

    def verify_employee_id(self, employee_id: str):
        time.sleep(1)
        return self.NATIONAL_ID.matching(have.text(employee_id))

    # Establishment Details
    def fill_field_company_email(self, data: str):
        s(self.FIELD_COMPANY_EMAIL).perform(command.js.set_value("")).type(data)

    def fill_field_role(self, data: str):
        s(self.FIELD_ROLE).perform(command.js.set_value("")).type(data)

    def fill_field_work_location(self, data: str):
        s(self.FIELD_WORK_LOCATION).perform(command.js.set_value("")).type(data)
        s(self.DROPDOWN_WORK_LOCATION).should(be.visible).ss("a").first.click()

    # Employee Details
    def fill_field_name(self, data: str):
        s(self.FIELD_NAME).perform(command.js.set_value("")).type(data)

    def select_dropdown_marital_status(self, data: str):
        s(self.DROPDOWN_MARITAL_STATUS).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def select_dropdown_nationality(self, data: str):
        s(self.DROPDOWN_NATIONALITY).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def fill_field_field_passport_no(self, data: str):
        s(self.FIELD_PASSPORT_NO).perform(command.js.set_value("")).type(data)

    def fill_field_field_passport_expiry_date(self, data: str):
        s(self.FIELD_PASSPORT_EXPIRY_DATE).perform(command.js.set_value("")).type(data)

    def fill_field_date_of_birth(self, data: str):
        s(self.FIELD_DATE_OF_BIRTH).perform(command.js.set_value("")).type(data)

    def fill_field_dropdown_gender(self, data: str):
        s(self.DROPDOWN_GENDER).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def fill_field_dropdown_religion(self, data: str):
        s(self.DROPDOWN_RELIGION).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def select_checkbox_confirmation(self):
        s(self.CHECKBOX_CONFIRMATION).click()

    def select_dropdown_education_level(self, data: str):
        s(self.DROPDOWN_EDUCATION_LEVEL).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def fill_field_major(self, data: str):
        s(self.FIELD_MAJOR).perform(command.js.set_value("")).type(data)
        ss(self.DROPDOWN_WORK_LOCATION)[1].should(be.visible).ss("a").first.click()

    def fill_field_iban_number(self, data: str):
        s(self.FIELD_IBAN_NUMBER).perform(command.js.set_value("")).type(data)

    def fill_field_mobile_number(self, data: str):
        s(self.FIELD_MOBILE_NUMBER).perform(command.js.set_value("")).type(data)

    def fill_field_email(self, data: str):
        s(self.FIELD_EMAIL).perform(command.js.set_value("")).type(data)

    def fill_field_occupation(self, data: str):
        s(self.FIELD_OCCUPATION).should(be.visible).perform(command.js.set_value("")).type(data)
        time.sleep(1)
        s(self.DROPDOWN_OCCUPATION).hover().click()

    def fill_field_job_title_en(self, data: str):
        s(self.FIELD_JOB_TITLE_EN).should(be.visible).perform(command.js.set_value("")).type(data)

    def fill_field_job_title_ar(self, data: str):
        s(self.FIELD_JOB_TITLE_AR).perform(command.js.set_value("")).type(data)

    def fill_field_employee_number(self, data: str):
        s(self.FIELD_EMPLOYEE_NUMBER).perform(command.js.set_value("")).type(data)

    def fill_field_contract_period(self, data: str):
        s(self.FIELD_CONTRACT_PERIOD).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def fill_field_trial_period(self, data: str):
        s(self.FIELD_TRIAL_PERIOD).perform(command.js.set_value("")).type(data)

    def select_type_of_work(self, data: str):
        s(self.DROPDOWN_CONTRACT_TYPE).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def fill_field_period(self, data: str):
        s(self.FIELD_PERIOD).perform(command.js.set_value("")).type(data)

    def fill_field_notice_period(self, data: str):
        s(self.FIELD_NOTICE_PERIOD).perform(command.js.set_value("")).type(data)

    def select_working_hours_type(self, data: str):
        s(self.DROPDOWN_WORK_HOURS_TYPE).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def fill_field_days_per_week(self, data: str):
        s(self.FIELD_DAYS_PER_WEEK).perform(command.js.set_value("")).type(data)

    def fill_field_daily_hours(self, data: str):
        s(self.FIELD_DAILY_HOURS).perform(command.js.set_value("")).type(data)

    def fill_field_hours_per_week(self, data: str):
        s(self.FIELD_HOURS_PER_WEEK).perform(command.js.set_value("")).type(data)

    def fill_field_annual_vacations_days(self, data: str):
        s(self.FIELD_ANNUAL_VACATIONS_DAYS).perform(command.js.set_value("")).type(data)

    def fill_field_basic_salary(self, data: str):
        s(self.FIELD_BASIC_SALARY).perform(command.js.set_value("")).type(data)

    def select_dropdown_salary_amount_type(self, data: str):
        s(self.DROPDOWN_SALARY_AMOUNT_TYPE).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def select_dropdown_salary_period(self, data: str):
        s(self.DROPDOWN_SALARY_PERIOD).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def fill_field_housing_allowance(self, data: str):
        s(self.FIELD_HOUSING_ALLOWANCE).perform(command.js.set_value("")).type(data)

    def select_dropdown_housing_allowance_type(self, data: str):
        s(self.DROPDOWN_HOUSING_ALLOWANCE_TYPE).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def select_dropdown_housing_allowance_frequency(self, data: str):
        s(self.DROPDOWN_HOUSING_ALLOWANCE_FREQUENCY).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def fill_field_transportation_allowance(self, data: str):
        s(self.FIELD_TRANSPORTATION_ALLOWANCE).perform(command.js.set_value("")).type(data)

    def select_dropdown_transportation_allowance_type(self, data: str):
        s(self.DROPDOWN_TRANSPORTATION_ALLOWANCE_TYPE).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def select_dropdown_transportation_allowance_frequency(self, data: str):
        s(self.DROPDOWN_TRANSPORTATION_ALLOWANCE_FREQUENCY).should(be.visible).all(
            "option"
        ).element_by(have.text(data)).click()

    # Financial Benefits
    def click_btn_add_financial_benefits(self):
        s(self.BTN_ADD_FINANCIAL_BENEFITS).click()

    def fill_field_benefit_name_en(self, data: str):
        s(self.FIELD_BENEFIT_NAME_EN).perform(command.js.set_value("")).type(data)

    def fill_field_benefit_name_an(self, data: str):
        s(self.FIELD_BENEFIT_NAME_AR).perform(command.js.set_value("")).type(data)

    def fill_field_amount(self, data: str):
        s(self.FIELD_AMOUNT).perform(command.js.set_value("")).type(data)

    def select_dropdown_benefit_type(self, data: str):
        s(self.DROPDOWN_BENEFIT_TYPE).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    def select_dropdown_benefit_frequency(self, data: str):
        s(self.DROPDOWN_BENEFIT_FREQUENCY).should(be.visible).all("option").element_by(
            have.text(data)
        ).click()

    # Additional Clauses
    def click_btn_add_additional_clauses(self):
        s(self.BTN_ADD_ADDITIONAL_CLAUSES).click()

    def select_checkboxes_article(self):
        for checkbox in ss(self.CHECKBOXES_ARTICLE):
            checkbox.click()

    def click_btn_modal_add_additional_clauses(self):
        s(self.BTN_MODAL_ADD_ADDITIONAL_CLAUSES).click()

    def fill_field_non_compete_agreement_period(self, data: str):
        s(self.FIELD_NON_COMPETE_AGREEMENT_PERIOD).perform(command.js.set_value("")).type(data)

    def fill_field_non_compete_agreement_field(self, data: str):
        s(self.FIELD_NON_COMPETE_AGREEMENT_FIELD).perform(command.js.set_value("")).type(data)

    def fill_field_non_compete_agreement_location(self, data: str):
        s(self.FIELD_NON_COMPETE_AGREEMENT_LOCATION).perform(command.js.set_value("")).type(data)

    def fill_field_non_disclosure_clause_period(self, data: str):
        s(self.FIELD_NON_DISCLOSURE_CLAUSE_PERIOD).perform(command.js.set_value("")).type(data)

    def fill_field_non_disclosure_clause_field(self, data: str):
        s(self.FIELD_NON_DISCLOSURE_CLAUSE_FIELD).perform(command.js.set_value("")).type(data)

    def fill_field_non_disclosure_clause_location(self, data: str):
        s(self.FIELD_NON_DISCLOSURE_CLAUSE_LOCATION).perform(command.js.set_value("")).type(data)

    def fill_field_amount_from_1st_party_to_2nd_party(self, data: str):
        s(self.FIELD_AMOUNT_FROM_1ST_PARTY_TO_2ND_PARTY).perform(command.js.set_value("")).type(
            data
        )

    def fill_field_amount_from_2nd_party_to_1st_party(self, data: str):
        s(self.FIELD_AMOUNT_FROM_2ND_PARTY_TO_1ST_PARTY).perform(command.js.set_value("")).type(
            data
        )

    # Additional Terms
    def click_btn_add_additional_terms(self):
        s(self.BTN_ADD_ADDITIONAL_TERMS).click()

    def click_btn_modal_add_additional_terms(self):
        s(self.BTN_MODAL_ADD_ADDITIONAL_TERMS).click()

    def fill_field_english_term(self, data: str):
        s(self.FIELD_ENGLISH_TERM).perform(command.js.set_value("")).type(data)

    def fill_field_arabic_term(self, data: str):
        s(self.FIELD_ARABIC_TERM).perform(command.js.set_value("")).type(data)

    def click_btn_remove_term(self):
        self.BTN_REMOVE_TERM.click()

    def click_btn_add_term(self):
        self.BTN_ADD_TERM.click()

    def click_btn_save_and_close(self):
        s(self.BTN_SAVE_AND_CLOSE).click()

    def refresh_if_not_employee_details(self, laborer_number: str):
        locator = s(self.LABORER_ID)
        for _ in range(5):
            self.proceed_2fa().click_btn_verify()
            self.click_btn_next()
            if locator.wait_until(be.visible):
                break
            browser.driver.refresh()
        s(self.LABORER_ID).should(have.exact_text(laborer_number))

    def verify_success_contract_creation(self, text: dict, locale: str):
        s(self.MSG_SUCCESS_CONTRACT).should(have.exact_text(text[locale]))

    def click_btn_review_view_template(self):
        self.BTN_REVIEW_VIEW_TEMPLATE.click()

    def view_template(self):
        self.TABLE.rows.first.ss(self.TEMPLATES_TABLE_ACTION).first.click()

    def edit_template(self):
        self.TABLE.rows.first.ss(self.TEMPLATES_TABLE_ACTION).second.click()

    def remove_template(self):
        self.TABLE.rows.first.ss(self.TEMPLATES_TABLE_ACTION)[2].click()

    def click_btn_delete_template(self):
        self.BTN_DELETE_TEMPLATE.click()

    def click_btn_modify(self):
        self.BTN_MODIFY.click()

    def click_btn_modal_delete_template(self):
        s(self.BTN_MODAL_DELETE_TEMPLATE).ss("button").first.click()

    def verify_successfully_removing_template(self):
        s(self.TOAST).should(have.exact_text(ContractManagement.MSG_SUCCESS_TEMPLATE_REMOVING))

    def verify_template_name(self, template_name: str):
        s(self.TEMPLATE_NAME).should(have.exact_text(template_name))
