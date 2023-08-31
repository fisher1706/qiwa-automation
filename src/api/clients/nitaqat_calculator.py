import allure

import config
from src.api.assertions.response_validator import ResponseValidator
from src.api.requests.nitaqat import Nitaqat


class NitaqatApi:
    def __init__(self, api):
        self.api = api

    @allure.step("POST /nitaqat-calculator :: calculate nitaqat")
    def calculate_nitaqat(self, new_expats, new_saudis, expect_code=200):
        body = Nitaqat.create_post_nitaqat(new_expats, new_saudis)
        response = self.api.post(
            url=config.qiwa_urls.api, endpoint="/nitaqat-calculator", json=body
        )
        ResponseValidator(response).check_status_code(
            name="POST /nitaqat-calculator", expect_code=expect_code
        )
