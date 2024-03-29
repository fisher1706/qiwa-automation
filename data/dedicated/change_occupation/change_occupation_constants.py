from dataclasses import dataclass


@dataclass
class Eligibility:
    ELIGIBLE = "Eligible"
    NOT_ELIGIBLE = "Not Eligible"


@dataclass
class EstablishmentStatus:
    EXISTING = "قائمة"


@dataclass
class Occupation:
    SUPERVISOR = "مشرف عمال"
    MANAGER_DIRECTOR = "مدير الادارة"
    INFORMATION_TECHNOLOGY_OPERATIONS_TECHNICIAN = "فني عمليات تقنية معلومات"
    SECRETARY_GENERAL_OF_A_SPECIAL_INTEREST_ORGANIZATION = "أمين عام منظمة ذات اهتمامات خاصة"
    PERSONAL_CARE_WORKER = "عامل عناية شخصية"
    ACCOUNTANT = "محاسب قانوني"
    GENERAL_DIRECTOR = "مدير عام"


@dataclass
class Label:
    ACTIONS = "Actions"
    ELIGIBILITY = "Eligibility"
    IQAMA_NUMBER = "Iqama number"
