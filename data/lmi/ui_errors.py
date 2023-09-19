from dataclasses import dataclass


@dataclass
class BaseErrors:
    QUESTION_MESSAGE = '//span[@class="ml-1"]'
    DIMENSION_MESSAGE = '//span[@class="error-message"]'


@dataclass
class DimensionErrors:
    required_en_name = {
        "text": "This Dimension name already exists",
        "locator": BaseErrors.DIMENSION_MESSAGE,
    }
    required_ar_name = {
        "text": "اسم البُعد المدخل موجود مسبقاً",
        "locator": BaseErrors.DIMENSION_MESSAGE,
    }


@dataclass
class QuestionErrors:
    invalid_question_weight = {
        "text": "Weight must be between 0 and 10",
        "locator": BaseErrors.QUESTION_MESSAGE,
    }
    invalid_answer_score = {
        "text": "Weight must be between 1 and 11",
        "locator": BaseErrors.QUESTION_MESSAGE,
    }
