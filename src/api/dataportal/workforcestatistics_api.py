from datetime import datetime, timedelta
from http import HTTPStatus

import allure
import jmespath
import requests

from src.api.dataportal.schemas.builder.data_portal_body import DataPortalBody
from src.api.http_client import HTTPClient
from utils.assertion import assert_status_code


class GetWorkForceStatisticsApi:
    ibm_url = "https://gw-apic.qiwa.info/takamol/staging"

    def __init__(self, api=HTTPClient()):
        self.all_values = []
        self.first_value = []
        self.api = api
        self.last_value = []
        self.converted_value = None
        self.last_quarter = None
        self.bearer_token = None
        self.max_date = None
        self.min_date = None
        self.as_of_today = None

    @allure.step("POST /workforcestatistics/v2/getworkforcestatistics")
    def post_workforcestatistics(
        self,
        endpoint_id,
        filtered_data,
        response_filter,
    ):
        json_body = DataPortalBody.get_work_force_statistics_body(endpoint_id, filtered_data)
        response = requests.post(
            url=self.ibm_url + "/workforcestatistics/v2/getworkforcestatistics",
            data=json_body,
            headers={"Authorization": self.bearer_token},
            timeout=5,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        self.response_filtration(jmespath.search(response_filter, response.json()))
        self.convert_value(self.last_value)

    def response_filtration(self, response):
        self.last_value = response[-1]
        self.first_value = response[0]
        response.sort(reverse=True)
        self.all_values = response
        if not (self.last_value and self.first_value):
            self.last_value = 0
            self.first_value = 0
        else:
            while isinstance(self.last_value and self.first_value, list):
                self.last_value = self.last_value[0]
                self.first_value = self.first_value[0]

    def convert_value(self, value):
        value = float(f"{value:.5g}")
        step = 0
        while value >= 1000:
            step = 1
            value /= 1000.0
        value = f"{value:.2f}"
        self.converted_value = f"{value.rstrip('0').rstrip('.')}{['', 'K', 'M', 'B', 'T'][step]}"

    def get_bearer_token(self):
        response = requests.post(
            self.ibm_url + "/takamol-oauth/oauth2/token",
            data=DataPortalBody.get_bearer_token_body(),
            timeout=5,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        self.bearer_token = f"{response.json()['token_type']} {response.json()['access_token']}"

    def get_max_date(self):
        date_format = "%Y-%m-%d"
        response = requests.post(
            url=self.ibm_url + "/workforcestatistics/v2/getworkforcestatistics",
            data=DataPortalBody.get_max_date_body(),
            headers={"Authorization": self.bearer_token},
            timeout=5,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        self.max_date = jmespath.search(
            "WFSResponse.response.fact.item[*].item[?name=='MAXDATE'].value", response.json()
        )[0][0]
        self.min_date = jmespath.search(
            "WFSResponse.response.fact.item[?name=='MINDATE'].value", response.json()
        )[0]
        self.last_quarter = (
            datetime.strptime(self.max_date, date_format) - timedelta(days=90)
        ).strftime(date_format)
        self.as_of_today = (
            datetime.strptime(self.max_date, date_format) + timedelta(days=30)
        ).strftime(date_format)


workforce_api = GetWorkForceStatisticsApi()
