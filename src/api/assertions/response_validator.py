import allure
from cerberus import Validator
from requests import Response

from utils.schema_parser import load_json_schema


class ResponseValidator:
    def __init__(self, response: Response):
        self.response = response

    def check_status_code(self, name: str, expect_code: int = 200):
        actual_code = self.response.status_code
        assert actual_code == expect_code, (
            f"Request for {name} failed.\n"
            f"Request URL: {self.response.request.url}\n"
            f"Request body: {self.response.request.body}\n"
            f"Expected status code: {expect_code}\n"
            f"Actual status code: {actual_code}\n"
            f"Reason: {self.response.reason}\n"
            f"Text: {self.response.text}"
        )
        return self

    @allure.step
    def check_response_schema(self, schema_name):
        schema = load_json_schema(f"response/{schema_name}")
        json_response = self.response.json()
        validator = Validator(schema, ignore_none_values=True)
        is_valid = validator.validate(json_response)
        assert is_valid, validator.errors
        return self
