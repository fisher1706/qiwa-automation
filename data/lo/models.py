from typing import Optional

from data.lo.constants import (
    InfoAboutVisit,
    OfficesFront,
    RegionFront,
    RequesterTypeId,
    ServicesFront,
    SubServicesFront,
    VisitStatus,
)


class Booking:
    appointment_id: Optional[int]
    appointment_date: str
    appointment_time: Optional[str]
    personal_number: str
    requester_name: Optional[str]
    requester_id: Optional[int]
    appointment_creation_date: Optional[str]

    appointment_office_id: Optional[int]
    appointment_service_id: Optional[int]
    appointment_time: Optional[str]
    appointment_date: str
    appointment_region_id: Optional[int]
    appointment_labor_office_id: Optional[int]
    appointment_sequence_number: Optional[int]
    appointment_status: Optional[VisitStatus]
    appointment_request_type: Optional[RequesterTypeId]
    appointment_access_error: Optional[str]
    appointment_access_error: Optional[None]

    appointment_establishment_name: Optional[str]
    appointment_full_establishment: Optional[str]
    appointment_region_front_en: RegionFront
    appointment_region_front_ar: Optional[str]

    appointment_office_front: OfficesFront
    appointment_status_ar: Optional[str]
    appointment_status_id: Optional[int]

    appointment_service_front_en: ServicesFront
    appointment_service_front_ar: Optional[str]
    appointment_service_id: Optional[int]

    appointment_sub_service_front_en: SubServicesFront
    appointment_sub_service_front_ar: Optional[str]
    appointment_sub_service_id: Optional[int]

    appointment_info_visit: Optional[InfoAboutVisit]


class Policies:
    company_name: str
    city_id: int
    city_name: str
    email: str
    phone: str
    working_hours_no: str
    ramadan_working_hours_no: str
    off_days: [str]
    vacation_days_no: int
    annual_vacation_days_no: int
    calendar_type: str


class Visas:
    nationality: str
    occupation: str
    employees_embassy: str
    gender: str
    religion: str
    number_of_visas: int
