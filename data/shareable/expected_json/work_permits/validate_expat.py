def invalid_expat_number_error(number: str) -> dict:
    return {
        "validation_result": False,
        "errors": {
            "code": "WP-003",
            "message_en": "Sorry, we cannot issue- renew working permit "
            "because the border ID or border number is invalid ",
            "message_ar": "عفوا، لا يمكن إصدار/تجديد رخصة عمل حيث أن رقم الإقامة/رقم الحدود للعامل غير صحيح",
        },
        "expat_number": number,
    }


def processing_work_permit_error(number: str) -> dict:
    return {
        "validation_result": False,
        "errors": {
            "code": "WP-010",
            "message_en": "Sorry, we cannot renew working permit "
            "since the laborer working permit is under processing ",
            "message_ar": "عفوا، العامل لديه رخصة عمل قيد السداد",
        },
        "expat_number": number,
    }


def not_your_establishment_laborer_error(number: str) -> dict:
    return {
        "validation_result": False,
        "errors": {
            "code": "WP-004",
            "message_en": "Sorry, we cannot issue- renew working permit "
            "because the laborer is not listed in your establishment ",
            "message_ar": "عفوا، لا يمكن إصدار/تجديد رخصة عمل حيث أن العامل غير مدرج ضمن عمالة منشأتك ",
        },
        "expat_number": number,
    }
