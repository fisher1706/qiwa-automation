import allure
import jmespath

import config
from src.api.assertions.response_validator import ResponseValidator
from src.api.lmi.requests.dimensions import Dimensions


class DimensionsApi:
    url = config.qiwa_urls.api

    def __init__(self, api):
        self.api = api
        self.dimension = None
        self.dimension_questions_id = []
        self.last_dimension_id = None

    @allure.step("POST /lmi-admin/dimension :: create dimension")
    def post_dimension(self, name_en, name_ar, cookies=None, expect_code=200):
        json_body = Dimensions.dimension_body(name_en, name_ar)
        response = self.api.post(
            url=self.url, endpoint="/lmi-admin/dimension", cookies=cookies, json=json_body
        )
        validator = ResponseValidator(response)
        validator.check_status_code(name="POST /lmi-admin/dimension", expect_code=expect_code)
        assert response.text == "success"

    @allure.step("GET /lmi-admin/dimension :: get last dimension id")
    def get_last_dimension_id(self, expect_code=200):
        dimensions_id = []
        response = self.api.get(url=self.url, endpoint="/lmi-admin/dimension")
        validator = ResponseValidator(response)
        validator.check_status_code(name="GET /lmi-admin/dimension", expect_code=expect_code)
        dimensions = response.json()
        for dimension in dimensions["data"]:
            dimensions_id.append(int(dimension["id"]))
        self.last_dimension_id = max(dimensions_id)
        return self

    @allure.step("GET /lmi-admin/dimension/dimension_id :: get dimension details")
    def get_dimension(
        self,
        dimension_id,
        surveys_id=None,
        expect_code=200,
        expect_schema="dimension_details.json",
    ):
        response = self.api.get(url=self.url, endpoint=f"/lmi-admin/dimension/{dimension_id}")
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="GET /lmi-admin/dimension/dimension_id", expect_code=expect_code
        )
        if expect_schema == "dimension_details.json":
            validator.check_response_schema(schema_name="dimension_details.json")
            self.dimension = response.json()
            if str(surveys_id) in self.dimension["data"]["attributes"]["surveys"]:
                for dimension_questions in self.dimension["data"]["attributes"]["surveys"][
                    str(surveys_id)
                ]:
                    self.dimension_questions_id.append(dimension_questions["survey_question_id"])
            else:
                self.dimension_questions_id = []
        else:
            validator.check_response_schema(schema_name="dimension_not_found.json")
            self.dimension = response.json()
        return self

    def get_all_dimensions(self, cookies=None, expect_code=200):
        response = self.api.get(
            url=self.url, endpoint="/lmi-admin/dimension?per=100&page=1", headers=cookies
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="GET /lmi-admin/dimension?per=100&page=1", expect_code=expect_code
        )
        return response.json()

    @allure.step("delete all dimensions")
    def delete_all_dimensions(self, cookies=None):
        all_dimensions_id = jmespath.search("data[*].id", self.get_all_dimensions(cookies))
        if all_dimensions_id is not None:
            for dimension_id in all_dimensions_id:
                self.del_dimension(dimension_id)

    @allure.step("DELETE /lmi-admin/dimension/dimension_id :: delete dimension")
    def del_dimension(self, dimension_id, expect_code=200):
        response = self.api.delete(url=self.url, endpoint=f"/lmi-admin/dimension/{dimension_id}")
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="DELETE /lmi-admin/dimension/dimension_id", expect_code=expect_code
        )
        assert response.text == "success"

    @allure.step("PUT /lmi-admin/surveys/surveys_id/dimension/dimension_id :: edit dimension")
    def put_dimension_names(self, name_en_edited, name_ar_edited, dimension_id, expect_code=200):
        json_body = Dimensions.dimension_body(name_en_edited, name_ar_edited)
        response = self.api.put(
            url=self.url, endpoint=f"/lmi-admin/dimension/{dimension_id}", json=json_body
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="PUT /lmi-admin/surveys/surveys_id/dimension/dimension_id",
            expect_code=expect_code,
        )
        assert response.text == "success"

    @allure.step(
        "PUT /lmi-admin/dimension/dimension_id/attach-question :: attach question to dimension"
    )
    def put_attach_question(self, dimension_id, survey_question_id, expect_code=200):
        json_body = Dimensions.attach_detach_question_body(survey_question_id)
        response = self.api.put(
            url=self.url,
            endpoint=f"/lmi-admin/dimension/{dimension_id}" f"/attach-question",
            json=json_body,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="PUT /lmi-admin/dimension/dimension_id/attach-question", expect_code=expect_code
        )
        assert response.text == "success"

    @allure.step(
        "PUT /lmi-admin/dimension/dimension_id/detach-question:: detach question to dimension"
    )
    def put_detach_question(self, dimension_id, survey_question_id, expect_code=200):
        json_body = Dimensions.attach_detach_question_body(survey_question_id)
        response = self.api.put(
            url=self.url,
            endpoint=f"/lmi-admin/dimension/{dimension_id}" f"/detach-question",
            json=json_body,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="PUT /lmi-admin/dimension/dimension_id/detach-question", expect_code=expect_code
        )
        assert response.text == "success"
