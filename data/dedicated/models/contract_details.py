from pydantic import BaseModel


class EstablishmentDetails(BaseModel):
    company_email: str = "test@test.test"
    role: str = "Role"
    work_location: str = "Riyadh"


class EmployeeDetails(BaseModel):
    name: str = "Name"
    marital_status: list = ["Other", "Single", "Married", "Divorced", "Widowed", "Separate"]
    nationality: str = "Ukrainian"
    passport_no: str = "1234567890"
    passport_expiry_date: str = "01-01-2100"
    date_of_birth: str = "01-01-1976"
    gender: str = "Male"
    religion: str = "Others"
    education_level: str = "Associate Diploma"
    major: str = "Social Sciences"
    mobile_number: str = "0512345678"
    email: str = "test@test.test"


class FinancialBenefits(BaseModel):
    name_english: str = "Name En"
    name_arabic: str = "-"
    amount: str = "400"
    benefit_type: str = "SAR"
    frequency_for_financial_benefits: str = "monthly"


class AdditionalClauses(BaseModel):
    non_compete_agreement_period: str = "1"
    non_compete_agreement_field: str = "field"
    non_compete_agreement_location: str = "location"

    non_disclosure_clause_period: str = "1"
    non_disclosure_clause_field: str = "field"
    non_disclosure_clause_location: str = "location"

    amount_from_1st_party_to_2nd_party: str = "1"
    amount_from_2nd_party_to_1st_party: str = "1"


class AdditionalTerms(BaseModel):
    additional_terms_en = "Additional Terms En"
    additional_terms_ar = "-"


class ContractDetails(BaseModel):
    occupation: str = "Software Tester"
    job_title_en: str = "Job Title"
    job_title_ar: str = "-"
    employee_number: str = "21"

    contract_period: list = ["Specified Period", "Non-specified Period"]
    period: str = "1"
    trial_period: str = "1"

    type_of_work: str = "Full-time contract"
    working_hours_type: list = ["daily", "weekly"]
    days_per_week: str = "1"
    daily_hours: str = "1"
    hours_per_week: str = "1"
    annual_vacations_days: str = "21"

    notice_period: str = "30"
    iban_number: str = "2980000528608010105925"

    basic_salary: str = "1500"
    type_for_basic_salary: str = "SAR"
    frequency_for_basic_salary: str = "monthly"

    housing_allowance: str = "400"
    type_for_housing_allowance: str = "SAR"
    frequency_for_housing_allowance: str = "monthly"

    transportation_allowance: str = "monthly"
    type_for_transportation_allowance: str = "SAR"
    frequency_for_transportation_allowance: str = "monthly"

    financial_benefits: FinancialBenefits = FinancialBenefits()
    additional_clauses: AdditionalClauses = AdditionalClauses()
    additional_terms: AdditionalTerms = AdditionalTerms()
