from dataclasses import dataclass

from data.data_portal.constants import Admin
from data.lmi.constants import (
    Actions,
    DimensionAction,
    DimensionsInfo,
    QuestionActions,
    SurveyResultFile,
    SurveysInfo,
    TargetGroups,
)
from src.api.lmi.requests.surveys import Surveys


@dataclass
class DimensionDataSet:
    dimension_action_data_ids = [
        "Create Dimension",
        "Edit Dimension",
        "Delete Dimension",
        "Cancel edit Dimension",
        "Cancel delete Dimension",
    ]
    dimension_action_data = (
        (
            Actions.CREATE,
            DimensionsInfo.NAME_EN_TEXT,
            DimensionsInfo.NAME_AR_TEXT,
            DimensionsInfo.CREATE_SUCCESS_MESSAGE,
        ),
        (
            Actions.EDIT,
            DimensionsInfo.NAME_EN_TEXT,
            DimensionsInfo.NAME_EN_TEXT_EDIT,
            DimensionsInfo.NAME_AR_TEXT_EDIT,
            DimensionsInfo.EDIT_SUCCESS_MESSAGE,
        ),
        (Actions.DELETE, DimensionsInfo.NAME_EN_TEXT, DimensionsInfo.DELETE_SUCCESS_MESSAGE),
        (
            DimensionAction.CANCEL_EDIT,
            DimensionsInfo.NAME_EN_TEXT,
            DimensionsInfo.NAME_EN_TEXT_EDIT,
            DimensionsInfo.NAME_AR_TEXT_EDIT,
        ),
        (DimensionAction.CANCEL_DELETE, DimensionsInfo.NAME_EN_TEXT),
    )

    invalid_dimension_names_value = (
        (" ", " "),
        (" ", DimensionsInfo.NAME_AR_TEXT),
        (DimensionsInfo.NAME_EN_TEXT, " "),
        (" ", DimensionsInfo.NAME_AR_TEXT),
        (DimensionsInfo.NAME_EN_TEXT, " "),
        (DimensionsInfo.NAME_EN_TEXT, "t1"),
        ("2t", DimensionsInfo.NAME_AR_TEXT),
        ("te", "st"),
        (DimensionsInfo.NAME_EN_TEXT, DimensionsInfo.NAME_EN_TEXT),
        (DimensionsInfo.NAME_AR_TEXT, DimensionsInfo.NAME_AR_TEXT),
        (DimensionsInfo.NAME_AR_TEXT, DimensionsInfo.NAME_EN_TEXT),
    )

    dimension_created_names_value = (
        (
            DimensionsInfo.NAME_EN_TEXT,
            DimensionsInfo.NAME_AR_TEXT_EDIT,
            DimensionsInfo.DIMENSION_MESSAGE_EN,
        ),
        (
            DimensionsInfo.NAME_EN_TEXT_EDIT,
            DimensionsInfo.NAME_AR_TEXT,
            DimensionsInfo.DIMENSION_MESSAGE_AR,
        ),
    )


@dataclass
class SurveyDataSet:
    survey_ids_data = (SurveysInfo.SURVEYS_SS_ID, SurveysInfo.SURVEYS_QPRO_ID)

    survey_data = (
        (SurveysInfo.SURVEYS_SS_ID, SurveyResultFile.SS_RESULT_XLS, TargetGroups.RETAIL_MULTI),
        (SurveysInfo.SURVEYS_QPRO_ID, SurveyResultFile.QPRO_RESULT_XLS, TargetGroups.RETAIL_MULTI),
    )

    survey_type_data = (SurveysInfo.SURVEYS_QPRO_ID, SurveysInfo.SURVEYS_SS_ID)

    survey_attribute_json = (
        # Committed due to affect third part QA team
        # (Surveys.individual_displayed_body(True), None),
        # (Surveys.individual_displayed_body(False), None),
        (Surveys.favorite_survey_body(False), False),
        (Surveys.favorite_survey_body(True), False),
        (Surveys.setup_target_group_body(TargetGroups.ALL), True),
        (Surveys.setup_target_group_body(TargetGroups.RETAIL), True),
        (Surveys.setup_target_group_body(TargetGroups.RETAIL_MULTI), True),
    )


@dataclass
class QuestionDataSet:
    question_value = float(5)

    question_action_data = (
        (QuestionActions.DETACH, DimensionsInfo.DETACH_QUESTION_SUCCESS_MESSAGE),
        (
            QuestionActions.ALREADY_ATTACHED,
            DimensionsInfo.NAME_EN_TEXT_EDIT,
            DimensionsInfo.ADD_QUESTION_SUCCESS_MESSAGE,
        ),
        (QuestionActions.CANCEL_ATTACH, DimensionsInfo.NAME_EN_TEXT_EDIT),
        (QuestionActions.CANCEL_DETACH, None),
    )

    setup_action_data = (
        (QuestionActions.RESET_WEIGHT, None),
        (QuestionActions.QUESTION_WEIGHT, DimensionsInfo.UPDATE_WEIGHT_SUCCESS),
        (QuestionActions.QUESTION_CODE, DimensionsInfo.UPDATE_CODE_SUCCESS),
        (QuestionActions.ANSWER_WEIGHT, DimensionsInfo.UPDATE_WEIGHT_SUCCESS),
        (QuestionActions.MAX_ANSWER_SCORE, DimensionsInfo.UPDATE_WEIGHT_SUCCESS),
    )

    setup_action_api_data = (
        (
            SurveysInfo.SURVEYS_QPRO_ID,
            SurveysInfo.QUESTION_QPRO_ID,
            question_value,
            SurveysInfo.QUESTION_QPRO_CHOICE_ID,
            question_value,
        ),
        (
            SurveysInfo.SURVEYS_SS_ID,
            SurveysInfo.QUESTION_SS_ID,
            question_value,
            SurveysInfo.QUESTION_SS_CHOICE_ID,
            question_value,
        ),
    )

    invalid_question_data = (10.1, ".", "")

    invalid_answer_data = (0, 0.9, 11.1, ".", "")

    invalid_code_data = ("", " ")


@dataclass
class ResultDataSet:
    result_action_data = (
        Actions.CREATE,
        (
            Actions.EDIT,
            f"{DimensionsInfo.NAME_EN_TEXT} {Actions.EDIT}",
            DimensionsInfo.EDIT_LINK_SUCCESS_MESSAGE,
        ),
        (Actions.DELETE, DimensionsInfo.NAME_EN_TEXT, DimensionsInfo.DELETE_LINK_SUCCESS_MESSAGE),
        (Actions.COUNTER, DimensionsInfo.COPY_LINK_MESSAGE),
    )


@dataclass
class AdminDataSet:
    criteria = (
        (Admin.AUTOMATION, None, None, None),
        (Admin.AUTOMATION, Admin.PUBLISHED, None, None),
        (Admin.AUTOMATION, None, Admin.ENGLISH_FILTER, None),
        (Admin.AUTOMATION, None, None, Admin.AUTOMATION),
        (Admin.AUTOMATION, Admin.PUBLISHED, Admin.ENGLISH_FILTER, None),
        (Admin.AUTOMATION, Admin.PUBLISHED, Admin.ARABIC_FILTER, None),
        (Admin.AUTOMATION, Admin.PUBLISHED, None, Admin.AUTOMATION),
        (Admin.AUTOMATION, None, Admin.ENGLISH_FILTER, Admin.AUTOMATION),
        (None, Admin.PUBLISHED, None, None),
        (None, Admin.PUBLISHED, Admin.ENGLISH_FILTER, None),
        (None, Admin.PUBLISHED, Admin.ARABIC_FILTER, None),
        (None, Admin.PUBLISHED, None, Admin.AUTOMATION),
        (None, Admin.PUBLISHED, Admin.ENGLISH_FILTER, Admin.AUTOMATION),
        (None, Admin.PUBLISHED, Admin.ARABIC_FILTER, Admin.AUTOMATION),
        (None, None, Admin.ENGLISH_FILTER, None),
        (None, None, Admin.ENGLISH_FILTER, Admin.AUTOMATION),
        (None, None, None, Admin.AUTOMATION),
    )


DISCORD_HOOKS = {
    # 'stage': {
    #         'lmi-daily-api': [
    #             'https://discord.com/api/webhooks/1027598125856211034/'
    #             '4pU1QkHNebHUltbCg1qmJzexNqGbjiaKImWeg2FyTrlo-coa5oblcLVUwvQir7cRpHWq',
    #             'https://discord.com/api/webhooks/1034899664438309035/'
    #             'oWHDmkocL5k9aHmzA9Ilc6FQ3APfuUHSKw0B9YYyB9VUPBAZ-GVsI-ZCNAuN1lbEcAhT'],
    #
    #         'lmi-daily-ui': [
    #             'https://discord.com/api/webhooks/1027598314612457543/'
    #             'FwXHyk0hQ1zGstlMen6xwpK_mX3MVqT_K6UIkiLs-d1A28A46WERQXqPCQvkF6jvaJdc',
    #             'https://discord.com/api/webhooks/1034899982051975168/'
    #             'HMx_mKCjMl7apNseej3BPZfGdbLdyCJbihoAYXI4goJn39sQyzCEgJ9xNvi_nah2yKHn'],
    #     }
    # }
    # """Temporary webhook for debugging"""
    "stage": {
        "lmi-daily-api": [
            "https://discord.com/api/webhooks/1028795100253392941/"
            "DcHbmFqTLfG__-i-hQq9oV9kRHWf53hzk4BhZ0OQsm8L5PTM-wrthMANAyaEmDtbcJ5O"
        ],
        "lmi-daily-ui": [
            "https://discord.com/api/webhooks/1028794186763345980/"
            "2HXA53PckEThe7017UeuP9xAAEdmWZWCVmtXBPhZAf3IB2mmGX0hnFvabj5xfYSJaq2o"
        ],
    }
}
