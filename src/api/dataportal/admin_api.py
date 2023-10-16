from http import HTTPStatus

import allure
import jmespath

import config
from src.api.http_client import HTTPClient
from utils.assertion import assert_status_code


class AdminApi:
    url = config.qiwa_urls.data_portal_admin_url

    def __init__(self, api=HTTPClient()):
        self.api = api
        self.uuid = []
        self.session_token = None
        self.category_id = None
        self.takeaway_section_id = None

    @allure.step("Get uuid by name")
    def get_uuid_report_by_name(self, cookies, name):
        response = self.api.get(
            url=self.url + f"/jsonapi/node/report?filter[title]={name}",
            headers={"Cookie": cookies},
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        self.uuid = jmespath.search("data[].id", response.json())

    def get_session_token(self, cookies):
        response = self.api.get(url=self.url + "/session/token", headers={"Cookie": cookies})
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        self.session_token = response.text

    @allure.step("Delete report")
    def delete_report(self, cookies):
        response = self.api.delete(
            url=self.url + f"/jsonapi/node/report/{self.uuid[0]}",
            headers={"X-CSRF-Token": self.session_token, "Cookie": cookies},
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.NO_CONTENT)

    def clear_test_report(self, cookies, name):
        self.get_uuid_report_by_name(cookies, name)
        if self.uuid:
            self.delete_report(cookies)

    @allure.step("Get category by name")
    def get_category_id_by_name(self, cookies, name):
        response = self.api.get(
            url=self.url + f"/jsonapi/taxonomy_term/category?filter[name]={name}",
            headers={"Cookie": cookies},
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        self.category_id = jmespath.search("data[].id", response.json())

    @allure.step("Delete category")
    def _delete_category(self, cookies):
        response = self.api.delete(
            url=self.url + f"/jsonapi/taxonomy_term/category/{self.category_id[0]}",
            headers={"X-CSRF-Token": self.session_token, "Cookie": cookies},
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.NO_CONTENT)

    def clear_test_category(self, cookies, name):
        self.get_category_id_by_name(cookies, name)
        if self.category_id:
            self._delete_category(cookies)

    @allure.step("Get Takeaway Section by name")
    def get_takeaway_section_id_by_name(self, cookies, name):
        response = self.api.get(
            url=self.url + f"/jsonapi/node/takeaway_section?filter[title]={name}",
            headers={"Cookie": cookies},
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        self.takeaway_section_id = jmespath.search("data[].id", response.json())

    @allure.step("Delete Takeaway Section")
    def delete_takeaway_section(self, cookies):
        response = self.api.delete(
            url=self.url + f"/jsonapi/node/takeaway_section/{self.takeaway_section_id[0]}",
            headers={"X-CSRF-Token": self.session_token, "Cookie": cookies},
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.NO_CONTENT)

    def clear_test_takeaway_section(self, cookies, name):
        self.get_takeaway_section_id_by_name(cookies, name)
        if self.takeaway_section_id:
            self.delete_takeaway_section(cookies)


admin_api = AdminApi()
