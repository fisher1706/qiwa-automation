from src.api.payloads.raw.user_management.edit_privileges import Privileges


def owner_subscription_payload(
    subscription_price,
    subscribed_user_personal_number,
    labor_office_id,
    sequence_number,
    privilege_ids,
):
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
