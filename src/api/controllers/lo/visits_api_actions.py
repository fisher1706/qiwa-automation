import allure

from data.lo.constants import VisitStatus
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
