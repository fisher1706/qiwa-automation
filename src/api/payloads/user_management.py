from src.api.payloads.raw.user_management.edit_privileges import Privileges


def owner_subscription_payload_for_new_subscription_type(
    subscription_price,
    subscribed_user_personal_number,
    labor_office_id,
    sequence_number,
    privilege_ids,
) -> dict:
    return {
        "totalFeeAmount": subscription_price,
        "lang": "en",
        "idnoEstablishmentRequests": {
            subscribed_user_personal_number: [
                Privileges(
                    laborOfficeId=labor_office_id,
                    sequenceNumber=sequence_number,
                    privilegeIds=privilege_ids,
                ).dict()
            ]
        },
    }


def owner_subscription_payload(
    subscription_price,
    subscribed_user_personal_number,
    labor_office_id,
    sequence_number,
    privilege_ids,
) -> dict:
    return {
        "totalFeeAmount": subscription_price,
        "lang": "en",
        "idno": subscribed_user_personal_number,
        "establishments": [
            Privileges(
                laborOfficeId=labor_office_id,
                sequenceNumber=sequence_number,
                privilegeIds=privilege_ids,
            ).dict()
        ],
    }
