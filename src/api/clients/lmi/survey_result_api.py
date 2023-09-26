import time
from pathlib import Path

import allure
import jmespath
import openpyxl

import config
from src.api.assertions.response_validator import ResponseValidator
from src.api.lmi.requests.surveys import Surveys


class SurveyResultApi:
    url = config.qiwa_urls.api

    def __init__(self, api):
        self.all_links_detail = None
        self.link_details = None
        self.link_id = None
        self.api = api
        self.parse_xls_result = {}
        self.xlsx_file = Path(__file__).parent.parent.parent.parent.parent.joinpath("data/files")

    @allure.step("POST /lmi-tracking/tracking-details :: create link")
    def post_link(
        self,
        survey_id,
        link_name,
        cookies=None,
        expect_code=200,
        expect_schema="link_details.json",
    ):
        json_body = Surveys.create_link_body(survey_id, link_name)
        response = self.api.post(
            url=self.url,
            endpoint="/lmi-tracking/tracking-details",
            json=json_body,
            cookies=cookies,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="GET /lmi-tracking/tracking-details", expect_code=expect_code
        )
        validator.check_response_schema(schema_name=expect_schema)
        self.link_details = response.json()
        self.link_id = jmespath.search("data.id", self.link_details)

    @allure.step("PATCH /lmi-tracking/tracking-details :: edit link")
    def patch_link(self, link_id, link_name, expect_code=200):
        json_body = Surveys.edit_link_body(link_id, link_name)
        response = self.api.patch(
            url=self.url, endpoint="/lmi-tracking/tracking-details", json=json_body
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="GET /lmi-tracking/tracking-details", expect_code=expect_code
        )
        assert response.text == "success"

    @allure.step("GET /lmi-tracking/tracking-details :: get link by id")
    def get_link(self, survey_id, link_id, cookies=None, expect_code=200):
        response = self.api.get(
            url=self.url,
            endpoint=f"/lmi-tracking/tracking-details?" f"survey_id={survey_id}&id={link_id}",
            cookies=cookies,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="GET /lmi-tracking/tracking-details ", expect_code=expect_code
        )
        self.link_details = response.json()

    @allure.step("GET /lmi-tracking/tracking-details :: get all links")
    def get_all_links(self, survey_id, cookies=None, expect_code=200):
        response = self.api.get(
            url=self.url,
            endpoint=f"/lmi-tracking/tracking-details?survey_id={survey_id}",
            cookies=cookies,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="GET /lmi-tracking/tracking-details ", expect_code=expect_code
        )
        self.all_links_detail = response.json()

    @allure.step("DELETE /lmi-tracking/tracking-details :: delete link")
    def del_link(self, link_id, expect_code=200):
        response = self.api.delete(
            url=self.url, endpoint=f"/lmi-tracking/tracking-details?id={link_id}"
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="DELETE /lmi-tracking/tracking-details ", expect_code=expect_code
        )
        assert response.text == "success"

    @allure.step("delete all links")
    def delete_all_links(self, survey_id, cookies=None):
        self.get_all_links(survey_id, cookies)
        all_link_id = jmespath.search("data[*].id", self.all_links_detail)
        if all_link_id:
            for link_id in all_link_id:
                self.del_link(link_id)

    @allure.step("POST /lmi-surveys/company-name :: post company name")
    def post_company_name(self, link_hex, expect_code=200):
        json_body = Surveys.company_name_body(link_hex)
        response = self.api.post(
            url=self.url, endpoint="/lmi-surveys/company-name", json=json_body
        )
        validator = ResponseValidator(response)
        validator.check_status_code(name="POST /lmi-surveys/company-name", expect_code=expect_code)

    @allure.step("GET lmi-admin/surveys/xls-responses :: download xls result")
    def get_download_xls_result(self, survey_id, name_xlsx, cookies=None, expect_code=200):
        for _ in range(10):
            response = self.api.get(
                url=self.url,
                endpoint=f"/lmi-admin/surveys/{survey_id}/xls-responses",
                cookies=cookies,
            )
            time.sleep(1)
            validator = ResponseValidator(response)
            validator.check_status_code(
                name="GET lmi-admin/surveys/xls-responses", expect_code=expect_code
            )
            if response.text.startswith("PK"):
                with open(self.xlsx_file.joinpath(name_xlsx), "wb") as content_xlsx:
                    content_xlsx.write(response.content)
                return
        raise AssertionError("File Error")

    @staticmethod
    def substitute_ar_values(data):
        for _, answer in data.items():
            for value in answer:
                if value == "نعم":
                    answer.insert(0, "Yes")
                if value == "لا":
                    answer.insert(0, "No")
                if value is None or value == "نعم" or value == "لا":
                    answer.remove(value)
                else:
                    continue
        return data

    def parse_excel_file(self, result_xlsx):
        self.parse_xls_result = self.substitute_ar_values(self.sort_data_in_xls(result_xlsx))

    def sort_data_in_xls(self, file_name):
        sheet = openpyxl.load_workbook(self.xlsx_file.joinpath(file_name)).active

        data = {}
        for i, row in enumerate(sheet.iter_rows(values_only=True)):
            if row[22] is None or row[23] is None or "Started" in row or row[27] is None:
                continue
            try:
                if int(row[27]) > 479999 or int(row[27]) < 450000:
                    continue
            except ValueError:
                pass
            start_column = 34
            if i == 0:
                data[row[0]] = []
                for item in row[start_column:]:
                    data[item] = []
            else:
                for key, value in data.items():
                    if list(data.keys()).index(key) == 0:
                        value.append(row[0])
                    else:
                        value.append(row[start_column])
                        start_column += 1
        return data
