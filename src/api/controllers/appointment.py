import allure

from data.shareable.saudization_certificate.saudi_certificate import AppointmentStatus
from src.api.clients.ibm import IbmApi


class AppointmentsApiController:
    @allure.step
    def check_invalid_response(self, user, service, expected_error_message: str):
        response = IbmApi().create_new_appointment(user, service)
        appointment_rs = AppointmentStatus.validate(
            response["CreateNewAppointmentRs"]["Header"]["ResponseStatus"]
        )
        assert expected_error_message == appointment_rs
