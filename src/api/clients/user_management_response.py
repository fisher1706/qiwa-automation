class UmResponse:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()

    def validate_response_schema(self, schema):
        schema.parse_obj(self.response_json)
        return self

    def validate_price_value_number_of_users(self, user, default_percent_value):
        assert(user.default_price * default_percent_value, self.response_json.get('totalFeeAmount'))
        return self
