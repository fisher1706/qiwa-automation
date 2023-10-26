from selene.support.shared.jquery_style import s

from src.ui.components.code_verification_box import CodeVerificationBox


# pylint: disable=too-few-public-methods
class MobileVerificationPopup:
    popup = CodeVerificationBox()
    popup.confirm_button = s("[form='otp-form']")
