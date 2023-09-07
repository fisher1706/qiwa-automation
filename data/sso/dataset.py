import dataclasses

from data.constants import UserInfo
from data.validation_message import ErrorMessage, SuccessMessage, ValidationMessage


@dataclasses.dataclass
class UserDataset:
    invalid_password = [
        [UserInfo.INVALID_PASSWORD, "", False, ValidationMessage.PASSWORD_VALIDATION],
        [
            UserInfo.CHANGED_PASSWORD,
            UserInfo.INVALID_PASSWORD,
            False,
            ValidationMessage.PASSWORD_CONFIRMATION,
        ],
        [UserInfo.PASSWORD, UserInfo.PASSWORD, True, ErrorMessage.OLD_PASSWORD],
    ]
    invalid_phone = [
        ["", ValidationMessage.PHONE_REQUIRED],
        ["00000000", ValidationMessage.SHORT_PHONE],
    ]
    invalid_sms = [
        ["123", ValidationMessage.SHORT_SMS, False],
        ["1234", ValidationMessage.INVALID_SMS, True],
    ]
    change_password = [
        [True, UserInfo.CHANGED_PASSWORD, SuccessMessage.LOGIN],
        [False, UserInfo.PASSWORD, ErrorMessage.INVALID_CREDENTIALS],
    ]
    invalid_email = [
        ["asdasd", "Invalid Domain Name"],
        ["@asd.asd", "Recipient is not valid"],
        ["asdasd@asd", "Invalid Domain Name"],
        ["asdasd@", "Recipient is not valid"],
        ["asdasd@@mail.col", "Recipient is not valid"],
        ["!@#$#$%%#\\", "Recipient is not valid"],
        [" ", "Recipient is not valid"],
        ["'aasdwdasd@sadasd.asd", "Recipient is not valid"],
    ]
    invalid_password_api = [
        ["", "Password is incorrect"],
        [UserInfo.INVALID_PASSWORD, "Password is incorrect"],
        [
            "77777777777777777777777777777777777777777777777777777777777777777",
            "Password is incorrect",
        ],
        ["!@#$%^'&*", "Password is incorrect"],
    ]
    invalid_password_laborer_sso_api = [
        ["", "Password is too short"],
        [UserInfo.INVALID_PASSWORD, "Not enough characters in password"],
        [
            "77777777777777777777",
            "Your password should be at least 8 characters long and contain an uppercase letter, a lowercase letter, "
            "a number, and a symbol",
        ],
        [
            "77777777777777777777777777777777777777777777777777777777777777777!As7777777777777777777777777777777777777",
            "Many repeating characters in password",
        ],
    ]
    invalid_phone_api = [
        "{{badPhone}}",
        "stri2ng",
        "@#$\\%_'",
        "15487954238476454654632424672342342423434234242468",
        " ",
        "{}",
        "nil",
    ]
