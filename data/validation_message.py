import dataclasses


@dataclasses.dataclass
class SuccessMessage:
    LOGIN = {"type": "success", "text": "You have successfully logged in"}
    CHANGE_PHONE = {"type": "success", "text": "Phone number was changed"}
    CHANGE_PASSWORD = {"type": "success", "text": "Password was changed. You can login now."}
    UNLOCK_ACCOUNT = {"type": "success", "text": "Your account has been unlocked"}
    REGISTRATION = {"type": "success", "text": "You successfully registered."}
    UPDATE_PHONE = {
        "type": "edit profile success",
        "text": "Phone number has been updated successfully",
    }
    SUBSCRIPTION = {"type": "success", "text": "You have successfully subscribed to Qiwa"}
    SUBSCRIPTION_CREATED = {
        "type": "subscription_success",
        "text": "Your subscription has been created",
    }
    SUBSCRIPTION_ACTIVATED = {
        "type": "subscription_success",
        "text": "Subscription has been activated successfully",
    }
    SUBSCRIPTION_EXTENDED = {
        "type": "subscription_success",
        "text": "Subscription has been extended successfully",
    }
    SUBSCRIPTION_TERMINATED = {"type": "", "text": "Subscription terminated"}
    UPDATE_EMAIL = {"type": "edit profile success", "text": "Email has been updated successfully"}
    NO_MESSAGE = {"type": "", "text": ""}
    VALID = {"type": "valid", "text": "Valid"}
    VALID_SECOND = {"type": "valid second", "text": "Valid"}
    PERMISSION = {"type": "permissions", "text": "Your permissions have been set"}
    VALIDATION_EMAIL_MESSAGE = {
        "type": "e-services resend confirmation email",
        "text": "Verification email was sent",
    }
    E_SERVICE_CREATED_MESSAGE = {
        "type": "e-services successfully created",
        "text": "E-service has been successfully created",
    }
    E_SERVICE_EDITED_MESSAGE = {
        "type": "e-services successfully edited",
        "text": "E-service has been successfully edited",
    }
    E_SERVICE_DELETED_MESSAGE = {
        "type": "e-service successfully deleted",
        "text": "The service has been successfully deleted",
    }
    E_SERVICE_CATEGORY_CREATED_MESSAGE = {
        "type": "e-service category successfully created",
        "text": "The category has been successfully saved",
    }
    E_SERVICE_CATEGORY_UPDATE_MESSAGE = "The category has been successfully updated"
    E_SERVICE_CATEGORY_DELETED = "The category has been successfully deleted"
    SPACE_CREATED_MESSAGE = {
        "type": "space successfully created",
        "text": "Space has been successfully created",
    }
    SPACE_EDIT_MESSAGE = {
        "type": "space successfully edited",
        "text": "Space has been successfully edited",
    }

    SPACE_DELETED_MESSAGE = {
        "type": "space successfully deleted",
        "text": "The space has been successfully deleted",
    }
    ET_REQUEST = {
        "type": "et request",
        "text": "Your Employees transfer – Laborer transfer request was successful!",
    }
    ET_LABORER_REQUEST = {
        "type": "et laborer request",
        "text": "The request accepted successfully",
    }
    ET_SPONSOR_REQUEST = {
        "type": "et sponsor request",
        "text": "The request has been approved successfully",
    }


@dataclasses.dataclass
class ValidationMessage:
    SHORT_AUTH_CODE = {
        "type": "validation",
        "text": "The Authentication code field must be at least 4 characters",
    }
    INVALID_USERNAME = {"type": "validation", "text": "Enter a valid username"}
    INVALID_PASSWORD = {"type": "validation", "text": "Enter a valid password"}
    SHORT_PHONE = {
        "type": "validation",
        "text": "The Phone number field must be numeric and contains exactly 9 digits",
    }
    SHORT_SMS = {
        "type": "validation",
        "text": "The Confirmation Code field must be numeric and contains exactly 4 " "digits",
    }
    SHORT_ABSHER = {
        "type": "validation",
        "text": "The Confirmation Code field must be numeric and contains exactly 6 " "digits",
    }
    INVALID_NID = {"type": "validation", "text": "Enter a valid National ID or Iqama"}
    PASSWORD_VALIDATION = {
        "type": "validation",
        "text": "Your password should have minimum 10 characters, include "
        "small letter, capital letter, number and symbol.",
    }
    PASSWORD_CONFIRMATION = {
        "type": "validation",
        "text": "The password confirmation does not match",
    }
    INVALID_EMAIL = {"type": "validation", "text": "The E-mail field must be a valid email"}
    INVALID_EDIT_EMAIL = {"type": "validation", "text": "The Email field must be a valid email"}
    PHONE_REQUIRED = {"type": "validation", "text": "The Phone number field is required"}
    INVALID_SMS = {
        "type": "validation sms",
        "text": "You entered the wrong code. Please, try again",
    }
    INVALID_CERTIFICATE_NUMBER = {
        "type": "certificate validation",
        "text": "The Number of Certificate field format " "is invalid",
    }
    REQUIRED_CERTIFICATE_NUMBER = {
        "type": "certificate validation",
        "text": "The Number of Certificate field is " "required",
    }
    INVALID_CERTIFICATE = {"type": "certificate error", "text": "Missing Parameters"}
    CONFIRM_EMAIL = {
        "type": "confirmation message",
        "text": "Once you verify your email, you'll receive the "
        "confirmation email and subscription invoice",
    }
    UNCONFIRMED_EMAIL = {
        "type": "e-services pop up email title",
        "text": "Please verify your registered email in " "Qiwa to be able to use the e-services",
    }
    VAT_ERROR = {"type": "", "text": "The VAT Number field is required"}
    VAT_LENGHT_ERROR = {"type": "", "text": "The VAT Number length must be 15"}
    ESTABLISHMENT_ADRESS_ERROR = {
        "type": "",
        "text": "You don’t have permission to edit these details. Please contact "
        "unified number manager.",
    }


@dataclasses.dataclass
class ErrorMessage:
    INVALID_SMS_N_TIMES = {
        "type": "absher many attempts error",
        "text": "Sorry, you have entered an incorrect code 4 times, please click on the link below "
        "to receive a new code.",
    }
    UNCONFIRMED_EMAIL = {
        "type": "unconfirmed email error",
        "text": "Please, login using your identity number",
    }
    INVALID_CREDENTIALS = {
        "type": "invalid credentials error",
        "text": "Login or password is incorrect",
    }
    LOCKED_ACCOUNT = {
        "type": "locked account error",
        "text": "Your account is locked, please check your email to unlock your account or click here "
        "to unlock it using Absher verification",
    }
    INVALID_OTP_N_TIMES = {
        "type": "otp many attempts error",
        "text": "Sorry, you have entered an incorrect code 4 times, please click on the link below "
        "to receive a new code.",
    }
    INVALID_OTP = {
        "type": "invalid otp error",
        "text": "You entered the wrong code. Please, try again",
    }
    INVALID_ABSHER = {
        "type": "invalid absher error",
        "text": "You entered the wrong code. Please, try again",
    }
    USED_PHONE = {
        "type": "error",
        "text": "The phone number you entered is already used in Qiwa Verification",
    }
    USED_EMAIL = {
        "type": "error",
        "text": "This email address has been registered, please use a different one",
    }
    USED_NID = {"type": "account already exist", "text": "NID/Iqama is already registered in Qiwa"}
    OLD_PASSWORD = {
        "type": "new password equals old",
        "text": "Sorry, you can't use your old password",
    }
    USER_SUBSCRIBED = {"type": "error", "text": "already subscribed"}
    SUBSCRIPTION_NOT_CREATED = {
        "type": "error",
        "text": "Sorry, the subscription is not done due to a payment issue!",
    }
    EMAIL_CONFIRMATION = {"type": "confirmation error", "text": "Please confirm your email"}
    NITAQAT_ERROR = {
        "type": "nitaqat error",
        "text": "رابط توثيق البريد الإلكتروني غير صالح! نأمل التحقق من البريد "
        "الإلكتروني الصحيح المسجل في حسابكم على قوى",
    }
    INVALID_USER = {
        "type": "error",
        "text": "User with ID 0000000000 is not registered in Qiwa. Please "
        "ensure user registers on qiwa.sa",
    }
    EMAIL_ALREADY_USED_MESSAGE_AR = {
        "type": "",
        "text": "هذا البريد الإلكتروني مستخدم بالفعل، يرجى إدخال بريد إلكتروني آخر",
    }
    INVALID_SPACE_ENGLISH_NAME = {
        "type": "invalid english name field format on space",
        "text": "The Name English field format is invalid",
    }
    ERROR_MESSAGE_WHEN_USER_TRIES_SUBSCRIBE_HIMSELF = {
        "type": "error",
        "text": "You have an active subscription. You "
        "can renew your subscription within "
        "one month of expiry date through "
        "“Subscriptions” page",
    }
    INVALID_RESTORE_PASSWORD_TOKEN = {
        "type": "error token",
        "text": "The link is invalid or expired. Please, try again.",
    }
    INVALID_RESTORE_PASSWORD_ABSHER_FIRST_ATTEMPT = {
        "type": "validation sms",
        "text": "2 attempts remaining",
    }
    INVALID_RESTORE_PASSWORD_ABSHER_SECOND_ATTEMPT = {
        "type": "validation sms",
        "text": "1 attempt remaining",
    }
    INVALID_RESTORE_PASSWORD_ABSHER_THIRD_ATTEMPT = {
        "type": "validation sms",
        "text": "Please wait 15 minutes and try again.",
    }
    INVALID_IDENTITY_NUMBER = {"type": "error", "text": "Identity number is invalid"}
    USER_IS_NOT_ELIGIBLE = {"type": "", "text": "User is not eligible"}
    NOT_ELIGIBLE_UM = {"type": "", "text": "User is not eligible for service"}
    NOT_ELIGIBLE_UM_AR = {"type": "", "text": "المستخدم ليس لديه الصلاحية للخدمة"}
    ET_LABORER_REQUEST = {
        "type": "et laborer request",
        "text": "The request rejected successfully",
    }
    ET_SPONSOR_REQUEST = {
        "type": "et sponsor request",
        "text": "The request has been rejected successfully",
    }

    TERMINATE_ERROR = {
        "type": "",
        "text": "Sorry, you can not update or terminate the subscription of the unified " "owner",
    }
