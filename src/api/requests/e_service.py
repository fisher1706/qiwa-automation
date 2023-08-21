from utils.random_manager import RandomManager
from utils.schema_parser import load_json_schema


class EService:
    @classmethod
    def create_e_service_body(cls, need_permission: bool) -> dict:
        name_generator = f"auto test {RandomManager.random_eng_string(5)}"
        service_code_generator = f"Autotest{RandomManager.random_eng_string(3)}"
        create_body = load_json_schema("create_e-service.json")
        create_body["data"]["attributes"]["title-en"] = name_generator
        create_body["data"]["attributes"]["service-code"] = service_code_generator
        create_body["data"]["attributes"]["needs-permission"] = need_permission
        return create_body

    @classmethod
    def update_e_service_body(cls, e_service_id) -> dict:
        update_body = load_json_schema("update_e-service.json")
        update_body["data"]["id"] = e_service_id
        update_body["data"]["attributes"]["id"] = e_service_id
        return update_body

    @classmethod
    def create_tag_body(cls) -> dict:
        create_body = load_json_schema("create_tag.json")
        return create_body

    @classmethod
    def update_tag_body(cls, tag_id) -> dict:
        update_body = load_json_schema("update_tag.json")
        update_body["data"]["id"] = tag_id
        update_body["data"]["attributes"]["id"] = tag_id
        return update_body
