from dataclasses import dataclass


@dataclass
class SearchBy:
    EMPLOYEE_NAME = "Employee name"
    EMPLOYEE_ID = "Employee ID"
    NATIONALITY = "Nationality"
    OCCUPATION = "Occupation"
    NOTES = "Notes"
