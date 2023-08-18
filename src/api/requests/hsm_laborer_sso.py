from helpers.schema_parser import load_json_schema


class LaborerSSOHsm:
    @classmethod
    def create_init_body(cls, personal_number, year, month, day) -> dict:
        body = load_json_schema("laborer_sso_hsm_init.json")
        body["data"]["attributes"]["personal-number"] = personal_number
        if year and month and day:
            body["data"]["attributes"]["birth-date"] = f"{year}-{month}-{day}"
        return body

    @classmethod
    def create_activate_body(cls, sms_code) -> dict:
        body = load_json_schema("laborer_sso_hsm_init.json")
        body["data"]["attributes"]["otp"] = sms_code
        return body

    @classmethod
    def phone_verification(cls, phone_number) -> dict:
        body = load_json_schema("laborer_sso_phone_verify.json")
        body["data"]["attributes"]["phone"] = phone_number
        return body

    @classmethod
    def email_pre_check(cls, user_email) -> dict:
        body = load_json_schema("laborer_sso_email.json")
        body["data"]["attributes"]["email"] = user_email
        return body
