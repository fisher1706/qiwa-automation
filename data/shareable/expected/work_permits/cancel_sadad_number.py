def transaction_already_canceled() -> dict:
    return {
        "code": "MOF00005 ",
        "english_msg": "Cannot be canceled, the payment entry transaction is canceled",
        "arabic_msg": "لا يمكن الإلغاء، معاملة سداد المدخلة ملغاة",
    }


def transaction_canceled_successfully(sadad_number: str) -> dict:
    return {
        "message_en": f"SADAD bill {sadad_number} has been canceled successfully",
        "message_ar": f"تم إلغاء معاملة سداد رقم {sadad_number} بنجاح"
    }
