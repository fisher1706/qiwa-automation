import datetime
from http import HTTPStatus

from dateutil.relativedelta import relativedelta

from data.visa.constants import DateFormats, VisaUser
from src.api.clients.visa_mock_api_client import VisaMockApiClient
from src.api.http_client import HTTPClient
from utils.assertion import assert_status_code
from utils.schema_parser import load_json_schema


class VisaMockApi:
    def __init__(self):
        self.api = VisaMockApiClient(HTTPClient())
        self.establishment_id = VisaUser.ESTABLISHMENT_ID
        self.visa_quantity = load_json_schema("visa_quantity.json")

    def setup_company(self, **kwargs):
        data = load_json_schema("setup_mock.json")
        start_date = datetime.date.today() + relativedelta(months=-6)
        end_date = datetime.date.today() + relativedelta(months=+6)
        data["company_settings"]["allowance_start_date"] = start_date.strftime(
            DateFormats.YYYYMMDD
        )
        data["company_settings"]["allowance_end_date"] = end_date.strftime(DateFormats.YYYYMMDD)
        for key, value in kwargs.items():
            data["company_settings"][key] = value
        response = self.api.setup(data)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    def teardown_company(self):
        data = load_json_schema("teardown_company.json")
        labor_office_id, sequence_number = self.establishment_id.split("-")
        data["labor_office_id"] = labor_office_id
        data["sequence_number"] = sequence_number
        response = self.api.teardown(data)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    def change_balance_request(self, ref_number, refund_id=1, status_id=1):
        data = load_json_schema("refund.json")
        data["status"] = status_id
        data["refund_status_id"] = refund_id
        response = self.api.balance_request(ref_number, data)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    def change_visa_request(self, border_number, status):
        data = load_json_schema("refund.json")
        data["status"] = status
        response = self.api.visa_request(border_number, data)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    def delete_company_address(self):
        response = self.api.delete_address()
        assert_status_code(response.status_code).in_(
            [HTTPStatus.OK, HTTPStatus.UNPROCESSABLE_ENTITY]
        )

    def change_visa_quantity(self, tier, amount):
        data = load_json_schema("visa_quantity.json")
        data["maximum_balance"] = amount
        data["extra_balance"] = amount
        response = self.api.visa_quantity(tier, data)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
