import allure

import config
from src.api.assertions.response_validator import ResponseValidator
from utils.json_search import search_in_json


class UsersApi:
    url = config.qiwa_urls.api

    def __init__(self, api):
        self.api = api

    @allure.step('GET user by id "{user_id}"')
    def get_user(self, user_id, expected_code=200):
        response = self.api.get(url=self.url, endpoint=f"/lo-users/{user_id}")
        validator = ResponseValidator(response)
        validator.check_status_code(name=f"Get user {user_id}", expect_code=expected_code)
        return response, response.json()

    @allure.step("GET users")
    def get_users(self, expected_code=200):
        response = self.api.get(url=self.url, endpoint="/lo-users")
        validator = ResponseValidator(response)
        validator.check_status_code(name="Get users", expect_code=expected_code)
        return response, response.json()

    @allure.step("Edit user with email, role, office")
    def edit_user(self, user_id, email=None, role_id=None, office_id=None, expected_code=200):
        payload = {
            "data": {
                "type": "lo-user",
                "id": user_id,
                "attributes": {
                    "personal-number": user_id,
                    "email": email,
                    "role-id": role_id,
                    "office-id": office_id,
                    "id": user_id,
                },
            }
        }
        response = self.api.put(url=self.url, endpoint="/lo-users", json=payload)
        validator = ResponseValidator(response)
        validator.check_status_code(name="Change user status", expect_code=expected_code)
        validator.check_response_schema(schema_name="lo_user.json")

    @allure.step("Add user")
    def add_user(self, user_id, email, role_id, office_id, expected_code=200):
        payload = {
            "data": {
                "type": "lo-user",
                "id": user_id,
                "attributes": {
                    "personal-number": user_id,
                    "email": email,
                    "role-id": role_id,
                    "office-id": office_id,
                    "id": user_id,
                },
            }
        }
        response = self.api.post(url=self.url, endpoint="/lo-users", json=payload)
        validator = ResponseValidator(response)
        validator.check_status_code(name="Change user status", expect_code=expected_code)
        validator.check_response_schema(schema_name="lo_user.json")

    @allure.step("Get user status")
    def get_user_status(self, user_id):
        _, content = self.get_user(user_id=user_id)
        return search_in_json('data[*].attributes."is-active"', content)

    @allure.step('Change user status to "{status}"')
    def change_user_status(self, user_id, status, expected_code=200):
        payload = {
            "data": {
                "id": user_id,
                "type": "lo-user",
                "attributes": {"id": user_id, "personal-number": user_id, "is-active": status},
            }
        }
        response = self.api.patch(url=self.url, endpoint="/lo-users/status", json=payload)
        validator = ResponseValidator(response)
        validator.check_status_code(name="Change user status", expect_code=expected_code)
        validator.check_response_schema(schema_name="lo_user.json")
