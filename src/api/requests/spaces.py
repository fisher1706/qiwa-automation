from utils.random_manager import RandomManager
from utils.schema_parser import load_json_schema


class Spaces:
    @classmethod
    def create_space_body(cls, space_type="space", enabled=True, user_type="user") -> dict:
        create_body = load_json_schema("create_space.json")
        create_body["data"]["type"] = space_type
        create_body["data"]["attributes"]["name"][
            "en"
        ] = f"auto test {RandomManager.random_eng_string(7)}"
        create_body["data"]["attributes"]["name"][
            "ar"
        ] = f"أختبارذاتي{RandomManager.random_ar_string(7)}"
        create_body["data"]["attributes"]["enabled"] = enabled
        create_body["data"]["attributes"]["redirect-key-name"] = RandomManager.random_eng_string(8)
        create_body["data"]["attributes"]["type"] = user_type
        return create_body

    @classmethod
    def update_space_body(
        cls, space_id, space_type="space", enabled=True, user_type="user"
    ) -> dict:
        update_body = load_json_schema("create_space.json")
        update_body["data"]["type"] = space_type
        update_body["data"]["id"] = space_id
        update_body["data"]["attributes"]["id"] = space_id
        update_body["data"]["attributes"]["name"][
            "en"
        ] = f"auto_test_{RandomManager.random_eng_string(7)}"
        update_body["data"]["attributes"]["name"][
            "ar"
        ] = f"auto_test_{RandomManager.random_ar_string(7)}"
        update_body["data"]["attributes"]["enabled"] = enabled
        update_body["data"]["attributes"]["redirect-key-name"] = RandomManager.random_eng_string(8)
        update_body["data"]["attributes"]["type"] = user_type
        return update_body
