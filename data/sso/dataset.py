import dataclasses

from data.constants import UserInfo
from data.validation_message import ErrorMessage, SuccessMessage, ValidationMessage


@dataclasses.dataclass
class UserDataset:
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
    invalid_phone_api = [
        "{{badPhone}}",
        "stri2ng",
        "@#$\\%_'",
        "15487954238476454654632424672342342423434234242468",
        " ",
        "{}",
        "nil",
    ]
