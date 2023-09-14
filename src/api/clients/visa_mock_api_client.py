import config
from data.visa.constants import VisaUser
from src.api.http_client import HTTPClient


class VisaMockApiClient:
    def __init__(self, client: HTTPClient):
        self.api_client = client
        self.api_url = config.settings.visa_mock_mlsd_url
        self.establishment_id = VisaUser.ESTABLISHMENT_ID
        self.setup_end_point = f"/api/company_settings/{self.establishment_id}"
        self.teardown_end_point = "/api/all_requests"
        self.refund_end_point = "/api/requests/{}"
        self.visa_end_point = "/api/visas/{}"
        self.delete_company_address_end_point = (
            f"/api/company_settings/{self.establishment_id}/company_address"
        )
        self.visa_quantity_end_point = f"/api/company_settings/{self.establishment_id}/tiers/"

    def setup(self, data):
        return self.api_client.put(self.api_url, self.setup_end_point, json=data)

    def teardown(self, data):
        return self.api_client.delete(self.api_url, self.teardown_end_point, json=data)

    def balance_request(self, ref_number, data):
        return self.api_client.put(self.api_url, self.refund_end_point.format(ref_number), data)

    def visa_request(self, border_number, data):
        return self.api_client.put(
            self.api_url, self.visa_end_point.format(border_number), json=data
        )

    def delete_address(self):
        return self.api_client.delete(self.api_url, self.delete_company_address_end_point)

    def visa_quantity(self, tier, data):
        return self.api_client.put(
            self.api_url, self.visa_quantity_end_point + str(tier), json=data
        )
