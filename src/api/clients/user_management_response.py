from decimal import Decimal, ROUND_HALF_UP

from requests import Response

from data.dedicated.models.user import User
from utils.assertion import assert_that


class UmResponse:
    def __init__(self, response: Response):
        self.response = response
        self.response_json = response.json()

    @staticmethod
    def dround(amount: float, num: int = 2):
        quantize = f'.{"1".zfill(num)}'
        return Decimal(f'{amount}').quantize(Decimal(quantize), rounding=ROUND_HALF_UP)

    def validate_response_schema(self, schema):
        schema.parse_obj(self.response_json)
        return self

    def validate_price_value_number_of_users(self, user: User, default_vat_value: float):
        assert_that(self.dround(user.default_price * default_vat_value * user.default_discount))\
            .equals_to(self.response_json.get("totalFeeAmount"))
        return self
