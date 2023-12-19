from src.api.payloads.raw.data import Data
from src.api.payloads.raw.root import Root
from src.api.payloads.raw.user_management.edit_privileges import Privileges
from src.api.payloads.raw.user_management.renew_owner_flows import (
    UpdateEstablishmentAddress,
)


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


def update_establishment_address_payload(
    additional_no: int,
    building_no: int,
    city_id: int,
    district_area: str,
    street_name: str,
    zip_code: int,
):
    attributes = UpdateEstablishmentAddress(
        additional_no=additional_no,
        building_no=building_no,
        city_id=city_id,
        district_area=district_area,
        street_name=street_name,
        zip_code=zip_code,
    )
    return Root(data=Data(type="establishment", attributes=attributes)).dict(by_alias=True)
