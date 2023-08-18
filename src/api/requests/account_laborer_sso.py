from helpers.schema_parser import load_json_schema


class LaborerSSOAccount:
    @classmethod
    def register_account(cls, account_object) -> dict:
        account_body = load_json_schema("laborer_sso_account.json")
        account_body["data"]["attributes"]["otp"] = account_object.confirmation_code
        account_body["data"]["attributes"]["birth-date"] = (
            f"{account_object.year}-{account_object.month}" f"-{account_object.day}"
        )
        account_body["data"]["attributes"]["email"] = account_object.email
        account_body["data"]["attributes"]["password"] = account_object.password
        account_body["data"]["attributes"]["password-confirm"] = account_object.password
        return account_body

    @classmethod
    def login_user(cls, login, password) -> dict:
        login_body = load_json_schema("laborer_sso_login.json")
        login_body["data"]["attributes"]["login"] = login
        login_body["data"]["attributes"]["password"] = password
        return login_body

    @classmethod
    def check_otp_code(cls, otp: str = "0000", otp_type: str = "otp") -> dict:
        check_otp_code_body = load_json_schema("laborer_sso_login_with_otp.json")
        check_otp_code_body["data"]["type"] = otp_type
        check_otp_code_body["data"]["attributes"]["otp"] = otp
        return check_otp_code_body

    @classmethod
    def change_password(cls, old_password, new_password, new_password_confirm) -> dict:
        body = load_json_schema("new_password_laborer_sso.json")
        body["data"]["attributes"]["password"] = old_password
        body["data"]["attributes"]["new_password"] = new_password
        body["data"]["attributes"]["password-confirm"] = new_password_confirm
        return body
