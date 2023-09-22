import allure

from data.lo.constants import EmployeeTransferStatuses, VisitStatus
from data.lo.models import Booking
from src.api.clients.lo.visits import VisitsApi


class VisitsApiActions(VisitsApi):
    @allure.step("I create new visit")
    def book_visit(
        self,
        office_id,
        service_id,
        region_id,
        sub_service_id,
        requester_type_id,
        visit_reason_id,
        timedelta=None,
        labor_office_id=None,
        sequence_number=None,
    ) -> Booking:
        # pylint: disable=duplicate-code
        self.get_valid_date(timedelta)
        self.post_visit(
            office_id=office_id,
            service_id=service_id,
            time=self.valid_time,
            date=self.valid_date,
            region_id=region_id,
            labor_office_id=labor_office_id,
            sequence_number=sequence_number,
            sub_service_id=sub_service_id,
            requester_type_id=requester_type_id,
            visit_reason_id=visit_reason_id,
        )
        appointment_options = self.get_appointment_info(self.appointment_id)
        assert appointment_options.appointment_office_id == office_id
        assert appointment_options.appointment_service_id == service_id
        assert appointment_options.appointment_time == self.valid_time
        assert appointment_options.appointment_date == self.valid_date
        assert appointment_options.appointment_region_id == region_id
        assert appointment_options.appointment_labor_office_id == labor_office_id
        assert appointment_options.appointment_sequence_number == sequence_number
        assert appointment_options.appointment_request_type == requester_type_id
        assert appointment_options.appointment_status == VisitStatus.ACTIVE
        return appointment_options

    @allure.step("I edit last visit")
    def edit_visit(
        self,
        user_id,
        office_id,
        service_id,
        region_id,
        sub_service_id,
        requester_type_id,
        labor_office_id=None,
        sequence_number=None,
        timedelta=None,
    ) -> Booking:
        # pylint: disable=duplicate-code
        self.get_active_appointment_id(user_id)
        self.get_valid_date(timedelta)
        self.put_edit_visit(
            office_id=office_id,
            service_id=service_id,
            time=self.edited_time,
            date=self.edited_date,
            region_id=region_id,
            labor_office_id=labor_office_id,
            sequence_number=sequence_number,
            sub_service_id=sub_service_id,
            requester_type_id=requester_type_id,
            appointment_id=self.active_appointment_id,
        )
        appointment_options = self.get_appointment_info(self.active_appointment_id)
        assert appointment_options.appointment_office_id == office_id
        assert appointment_options.appointment_service_id == service_id
        assert appointment_options.appointment_time == self.edited_time
        assert appointment_options.appointment_date == self.edited_date
        assert appointment_options.appointment_region_id == region_id
        assert appointment_options.appointment_request_type == requester_type_id
        assert appointment_options.appointment_status == VisitStatus.ACTIVE
        return appointment_options

    @allure.step("Cancel visit")
    def cancel_active_visit(self, user_id, cookies=None) -> None:
        self.get_active_appointment_id(user_id, cookies)
        if self.active_appointment_id:
            self.delete_visit(self.active_appointment_id, cookies)
            appointment_options = self.get_appointment_info(self.active_appointment_id)
            assert appointment_options.appointment_status == VisitStatus.CANCELED

    @allure.step("I get appointment info using lo agent system")
    def get_appointment(
        self, office_id, service_id, region_id, labor_office_id, sequence_number, visit_status
    ) -> Booking:
        self.post_lo_otp_auth()
        appointment_options = self.get_appointment_info(self.appointment_id)
        assert appointment_options.appointment_office_id == office_id
        assert appointment_options.appointment_service_id == service_id
        assert appointment_options.appointment_time == self.valid_time
        assert appointment_options.appointment_date == self.valid_date
        assert appointment_options.appointment_region_id == region_id
        assert appointment_options.appointment_labor_office_id == labor_office_id
        assert appointment_options.appointment_sequence_number == sequence_number
        assert appointment_options.appointment_status == visit_status
        return appointment_options

    @allure.step("I unprocess appointment")
    def unprocess_appointment(self, user_id) -> Booking:
        self.post_lo_otp_auth()
        self.get_active_appointment_id(user_id)
        self.post_appointment_process(self.active_appointment_id)
        self.delete_appointment_process()
        appointment_options = self.get_appointment_info(self.active_appointment_id)
        assert appointment_options.appointment_status == VisitStatus.DONE
        return appointment_options

    @allure.step("I submit LO Policies request")
    def submit_lo_policies_request(
        self, establishment_name, email, phone, calendar_type, service_type
    ):
        self.post_lo_otp_auth()
        self.post_appointment_process(self.appointment_id)
        self.post_otp_custom(self.appointment_id, service_type)
        first_city_id, _ = self.get_cities()
        self.post_lo_policies_request(
            company_name=establishment_name,
            city=first_city_id,
            email=email,
            phone=phone,
            off_day=self.current_day,
            calendar_type=calendar_type,
        )

    @allure.step("I submit LO Employee Transfer request within unified number establishments")
    def submit_lo_et_request_unified_number(
        self, personal_number, labor_office_id, sequence_number, establishment_name, service_type
    ):
        self.post_lo_otp_auth()
        self.post_appointment_process(self.appointment_id)
        self.get_employee_info(personal_number)
        self.post_otp_custom(self.appointment_id, service_type)
        self.post_new_contract(personal_number)
        self.post_employee_trans_request_unified_number(
            dest_establishment_name=establishment_name,
            dest_labor_office_id=labor_office_id,
            dest_sequence_number=sequence_number,
            personal_number=personal_number,
            employee_name=self.employee_name,
            nationality_code=self.nationality_code,
            source_labor_office_id=self.source_labor_office_id,
            source_sequence_number=self.source_sequence_number,
        )
        self.post_cancel_et_request(self.request_number)
        status = self.get_employee_transfer_request_by_personal_number(personal_number)[
            "attributes"
        ]["status-name-en"]
        assert status == EmployeeTransferStatuses.CANCELED_BY_NEW_EMPLOYEE.value

    @allure.step("I submit LO Employee Transfer request from another business owner")
    def submit_lo_et_request_another_business_owner(
        self,
        personal_number,
        birth_date,
        labor_office_id,
        sequence_number,
        establishment_name,
        service_type,
    ):
        self.post_lo_otp_auth()
        self.post_appointment_process(self.appointment_id)
        self.post_employee_info_validate(personal_number, birth_date)
        self.post_otp_custom(self.appointment_id, service_type)
        self.post_new_contract(personal_number)
        self.post_employee_trans_request_another_business_owner(
            establishment_name,
            labor_office_id,
            sequence_number,
            personal_number,
            self.employee_name,
            self.nationality_code,
            self.date_of_expire,
            self.source_establishment_name,
            self.nationality_name_ar,
            self.nationality_name_en,
            self.establishment_id,
        )
        self.post_cancel_et_request(self.request_number)
        status = self.get_employee_transfer_request_by_personal_number(personal_number)[
            "attributes"
        ]["status-name-en"]
        assert status == EmployeeTransferStatuses.CANCELED_BY_NEW_EMPLOYEE.value

    @allure.step("I submit LO Visa request")
    def submit_visas_request(
        self,
        gender_id,
        occupation_id,
        nationality_id,
        embassy_id,
        religion_id,
        visas_amount,
        establishment_id,
        type_id,
        service_type,
    ):
        # pylint: disable=duplicate-code
        self.post_lo_otp_auth()
        self.post_appointment_process(self.appointment_id)
        self.post_otp_custom(self.appointment_id, service_type)
        self.post_lo_visa_request(
            gender_id,
            occupation_id,
            nationality_id,
            embassy_id,
            religion_id,
            visas_amount,
            establishment_id,
            type_id,
        )

    @allure.step("Cancel Issued Visas Request")
    def cancel_issued_visas_request(self, border_number, service_type):
        self.post_lo_otp_auth()
        self.post_appointment_process(self.appointment_id)
        self.post_otp_custom(self.appointment_id, service_type, border_number)
        self.post_lo_cancel_issued_visas(border_number)

    @allure.step("Terminate Establishing Period")
    def terminate_establish_period_visas(self, service_type):
        self.post_lo_otp_auth()
        self.post_appointment_process(self.appointment_id)
        self.post_otp_custom(self.appointment_id, service_type)
        # TODO: Add request after finding appropriate test data
