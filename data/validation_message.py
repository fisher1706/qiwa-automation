import dataclasses


@dataclasses.dataclass
class SuccessMessage:
    LOGIN = {"type": "success", "text": "You have successfully logged in"}
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
    E_SERVICE_CATEGORY_UPDATE_MESSAGE = "The category has been successfully updated"
    E_SERVICE_CATEGORY_DELETED = "The category has been successfully deleted"
    SPACE_CREATED_MESSAGE = "Space has been successfully created"
    SPACE_EDIT_MESSAGE = "Space has been successfully edited"

    SPACE_DELETED_MESSAGE = "The space has been successfully deleted"
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
    SHORT_PHONE = {
        "type": "validation",
        "text": "The Phone number field must be numeric and contains exactly 9 digits",
    }
    SHORT_SMS = {
        "type": "validation",
        "text": "The Confirmation Code field must be numeric and contains exactly 4 " "digits",
    }
    PASSWORD_VALIDATION = {
        "type": "validation",
        "text": "Your password should have minimum 10 characters, include "
        "small letter, capital letter, number and symbol.",
    }
    PASSWORD_CONFIRMATION = {
        "type": "validation",
        "text": "The password confirmation does not match",
    }
    PHONE_REQUIRED = {"type": "validation", "text": "The Phone number field is required"}
    INVALID_SMS = {
        "type": "validation sms",
        "text": "You entered the wrong code. Please, try again",
    }


@dataclasses.dataclass
class ErrorMessage:
    INVALID_CREDENTIALS = {
        "type": "invalid credentials error",
        "text": "Login or password is incorrect",
    }
    OLD_PASSWORD = {
        "type": "new password equals old",
        "text": "Sorry, you can't use your old password",
    }
    INVALID_SPACE_ENGLISH_NAME = "The Name English field format is invalid"
    ET_LABORER_REQUEST = {
        "type": "et laborer request",
        "text": "The request rejected successfully",
    }
    ET_SPONSOR_REQUEST = {
        "type": "et sponsor request",
        "text": "The request has been rejected successfully",
    }
