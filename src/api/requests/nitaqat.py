from utils.schema_parser import load_json_schema


class Nitaqat:
    @classmethod
    def create_post_nitaqat(cls, new_expats, new_saudis) -> dict:
        account_body = load_json_schema("nitaqat.json")
        account_body["new_number_expats"] = new_expats
        account_body["new_number_saudis"] = new_saudis
        return account_body
