from dataclasses import dataclass


@dataclass
class UserInfo:
    LMI_ADMIN_LOGIN = "1103410617"
    LMI_USER_LOGIN = "1095259030"
    DEFAULT_PASSWORD = "123456789aA@"
    DEFAULT_PASSWORD_API = "123456789aA@"
    DEFAULT_OTP_CODE = "0000"


@dataclass
class SurveysInfo:
    USER_ID_QPRO = 4000326
    STAGE_ENV_SPARROW = 367030
    STAGE_ENV_QPRO = 3391739
    SURVEYS_QPRO_ID = 79
    SURVEYS_SS_ID = 80
    QUESTION_QPRO_CHOICE_ID = "22841"
    QUESTION_QPRO_ID = 3182
    QUESTION_SS_CHOICE_ID = "22873"
    QUESTION_SS_ID = 3183
    SURVEY_NAME = "Survey Test"
    SURVEY_SPARROW_OPTION = "Survey Sparrow"
    SURVEY_QPRO_OPTION = "Question Pro"
    SURVEY_QPRO_NAME = "Auto test Question Pro"
    SURVEY_SS_NAME = "Auto test Survey Sparrow"


@dataclass
class DimensionsInfo:
    NAME_EN_TEXT = "AUTOMATION TEST"
    NAME_EN_TEXT_EDIT = "AUTOMATION TEST EDIT"
    NAME_EN_TEXT_EXTRA = "AUTOMATION TEST EXTRA"
    NAME_EN_CODE = [65, 85, 84, 79, 77, 65, 84, 73, 79, 78, 32, 84, 69, 83, 84]
    NAME_EN_CODE_EDIT = [
        65,
        85,
        84,
        79,
        77,
        65,
        84,
        73,
        79,
        78,
        32,
        84,
        69,
        83,
        84,
        32,
        69,
        68,
        73,
        84,
    ]
    NAME_EN_CODE_EXTRA = [
        65,
        85,
        84,
        79,
        77,
        65,
        84,
        73,
        79,
        78,
        32,
        84,
        69,
        83,
        84,
        32,
        69,
        88,
        84,
        82,
        65,
    ]
    NAME_AR_TEXT = "اختبار الأتمتة"
    NAME_AR_TEXT_EDIT = "تحرير اختبار الأتمتة"
    NAME_AR_TEXT_EXTRA = "اختبار الأتمتة الإضافي"

    CREATE_SUCCESS_MESSAGE = "Dimension was successfully created"
    EDIT_SUCCESS_MESSAGE = "Dimension was successfully updated"
    DELETE_SUCCESS_MESSAGE = "Dimension was successfully deleted"
    DETACH_QUESTION_SUCCESS_MESSAGE = "Question was successfully removed"
    ADD_QUESTION_SUCCESS_MESSAGE = "Question was successfully added"
    CREATE_LINK_SUCCESS_MESSAGE = "Link was successfully saved"
    DELETE_LINK_SUCCESS_MESSAGE = "Link was successfully deleted"
    EDIT_LINK_SUCCESS_MESSAGE = "Link was successfully updated"
    RECALCULATION_SUCCESS_MESSAGE = "Calculation finished"
    PUBLISHING_SUCCESS_MESSAGE = "Results were published"
    UPDATE_WEIGHT_SUCCESS = "Weights were successfully updated"
    UPDATE_CODE_SUCCESS = "Question code was successfully updated"
    COPY_LINK_MESSAGE = "Link was copied to clipboard"


@dataclass
class TargetGroups:
    ALL = ""
    RETAIL = [1]
    RETAIL_MULTI = [1, 2, 3]


@dataclass
class SurveyResultFile:
    SS_RESULT_XLS = "result_ss.xlsx"
    QPRO_RESULT_XLS = "result_qp.xlsx"


@dataclass
class LandingInfo:
    WORK_ENVIRONMENT_QUALITY_INDEX_BLOCK = "Work Environment Quality Index"
    LABOR_MARKET_STATISTICS_BLOCK = "Labor Market Statistics"


@dataclass
class Actions:
    COUNTER = "Counter"
    CREATE = "Create"
    EDIT = "Edit"
    DELETE = "Delete"


@dataclass
class DimensionAction:
    CANCEL_DELETE = "Cancel delete dimension"
    CANCEL_EDIT = "Cancel edit dimension"
    CREATE_INVALID = "Create dimension with invalid values"
    EDIT_INVALID = "Edit dimension with invalid values"


@dataclass
class QuestionActions:
    TEST_QUESTION = "Autotest question"
    ATTACH = "Attach"
    DETACH = "Detach"
    ALREADY_ATTACHED = "Already attached"
    CANCEL_ATTACH = "Cancel Attach"
    CANCEL_DETACH = "Cancel Detach"
    MAX_ANSWER_SCORE = "calculation_max_answer_score"
    QUESTION_CODE = "change_question_code"
    ANSWER_WEIGHT = "change_answer_weight"
    QUESTION_WEIGHT = "change_question_weight"
    RESET_WEIGHT = "reset_weight"

    INVALID_QUESTION_VALUE = "invalid_question_value"
    INVALID_ANSWER_SCORE = "invalid_answer_score"
    INVALID_QUESTION_CODE = "invalid_question_code"
