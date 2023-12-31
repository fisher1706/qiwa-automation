from src.api.payloads.raw.sso.nafath import CallBack
from src.api.payloads.raw.sso.sso_oauth import Hsm
from src.api.payloads.sso.sso_attributes_data import login_attributes


def init_nafath_logit(personal_number) -> dict:
    attributes = Hsm(personal_number=personal_number)
    return login_attributes(attributes).dict(exclude_unset=True, by_alias=True)


def nafath_callback(trans_id: str, status: str) -> dict:
    attributes = CallBack(transId=trans_id, status=status)
    return attributes.dict()
