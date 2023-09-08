import allure

from src.api.clients.lo.services import ServicesApi
from utils.json_search import search_in_json


class ServiceApiActions(ServicesApi):
    @allure.step("I create new service")
    def create_service(self, requester_type_id, name_en, name_ar):
        self.post_service(requester_type_id, name_en, name_ar)
        last_service_id = self.get_last_service_id()
        self.post_sub_service(requester_type_id, name_en, name_ar, service_id=last_service_id)
        self.get_last_service(last_service_id)
        name_en_json = search_in_json('*."name-en"', self.last_service)
        name_ar_json = search_in_json('*."name-ar"', self.last_service)
        requester_type_id_json = search_in_json('*."requester-type-id"', self.last_service)
        assert name_en_json == name_en
        assert name_ar_json == name_ar
        assert requester_type_id_json == requester_type_id

    @allure.step("I edit names of later service")
    def edit_service(self, requester_type_id, name_en, name_ar):
        last_service_id = self.get_last_service_id()
        self.put_edit_service(requester_type_id, name_en, name_ar, service_id=last_service_id)
        self.get_last_service(last_service_id)
        name_en_json = search_in_json('*."name-en"', self.last_service)
        name_ar_json = search_in_json('*."name-ar"', self.last_service)
        assert name_en_json == name_en
        assert name_ar_json == name_ar

    @allure.step("I edit names of later service")
    def edit_sub_service(self, requester_type_id, name_en, name_ar):
        last_service_id = self.get_last_service_id()
        self.put_edit_sub_service(
            requester_type_id,
            name_en,
            name_ar,
            service_id=last_service_id,
            sub_service_id=self.last_sub_service_id,
        )
        self.get_last_service(last_service_id)
        name_en_json = search_in_json('*."name-en"', self.last_sub_service)
        name_ar_json = search_in_json('*."name-ar"', self.last_sub_service)
        active = search_in_json('*."is-active"', self.last_sub_service)
        assert name_en_json == name_en
        assert name_ar_json == name_ar
        assert active is False

    @allure.step("I get current status, reversed it and setup for service")
    def change_status_service(self, requester_type_id, name_en, name_ar):
        last_service_id = self.get_last_service_id()
        self.get_last_service(last_service_id)
        reverse_service_status = self.service_status is False
        self.put_service_status(
            requester_type_id,
            name_en,
            name_ar,
            service_id=last_service_id,
            service_status=reverse_service_status,
        )
        self.get_last_service(last_service_id)
        reverse_service_status_json = search_in_json('*."is-active"', self.last_service)
        assert reverse_service_status_json == reverse_service_status
        self.put_service_status(
            requester_type_id, name_en, name_ar, last_service_id, not self.service_status
        )
