import allure

import config
from data.constants import Language
from src.api.assertions.response_validator import ResponseValidator
from src.api.requests.spaces import Spaces


class SpacesApi:
    url = config.qiwa_urls.api

    def __init__(self, api):
        self.api = api
        self.space_id = ""
        self.space_title = ""

    @allure.step("GET /spaces :: get spaces")
    def get_spaces(self, expect_code=200):
        response = self.api.get(url=self.url, endpoint="/admin/spaces")
        ResponseValidator(response).check_status_code(
            name="Get spaces data", expect_code=expect_code
        )

    @allure.step("GET /spaces/id :: get space")
    def check_space_status(self, expect_code=200, expect_status=True):
        response = self.api.get(url=self.url, endpoint=f"/admin/spaces/{self.space_id}")
        if expect_code == 200:
            ResponseValidator(response).check_status_code(
                name="Get spaces data", expect_code=expect_code
            )
            json = response.json()
            status = json["data"]["attributes"]["enabled"]
            assert self.space_id == json["data"]["id"]
            assert status == expect_status
        else:
            assert expect_code == 404, f"The space with {self.space_id} is not deleted"

    @allure.step
    def create_space(
        self,
        body: bool = True,
        expect_code: int = 201,
        space_type: str = "space",
        enabled: bool = True,
        user_type: str = "user",
    ) -> None:
        json_body = (
            Spaces.create_space_body(space_type=space_type, enabled=enabled, user_type=user_type)
            if body
            else "{}"
        )
        response = self.api.post(url=self.url, endpoint="/admin/spaces", json=json_body)
        validator = ResponseValidator(response)
        if expect_code == 201:
            validator.check_status_code(name="Create space", expect_code=expect_code)
            json = response.json()
            self.space_id = json["data"]["id"]
            self.space_title = json["data"]["attributes"]["name"][Language.EN]
        else:
            validator.check_status_code(name="Create space", expect_code=expect_code)

    @allure.step("PATCH /admin/spaces/id :: update space")
    def update_e_service(self, enabled=True):
        update_data = Spaces.update_space_body(self.space_id, enabled=enabled)
        response = self.api.patch(
            url=self.url, endpoint=f"/admin/spaces/{self.space_id}", json=update_data
        )
        try:
            ResponseValidator(response).check_status_code(name="Update space", expect_code=200)
        except AssertionError as err:
            raise AssertionError("The data with id of the space is missing") from err

    @allure.step("DELETE /admin/spaces/id :: delete space")
    def delete_space_request(self):
        response = self.api.delete(url=self.url, endpoint=f"/admin/spaces/{self.space_id}")
        try:
            ResponseValidator(response).check_status_code(name="Delete spaces", expect_code=200)
        except AssertionError as err:
            raise AssertionError("The data with id of the space is missing") from err
