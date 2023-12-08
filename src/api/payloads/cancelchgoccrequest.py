from src.api.payloads.ibm.cancelchgoccrequest import Body, CancelChangeOccupationRequestLORqPayload, CancelChangeOccupationRequestLORq
from src.api.payloads.ibm.header import Header, UserInfo


def cancel_change_occupation_request_payload(request_number: str) -> dict:
    return CancelChangeOccupationRequestLORqPayload(
        CancelChangeOccupationRequestLORq=CancelChangeOccupationRequestLORq(
            Header=Header(
                TransactionId="0",
                ChannelId="Qiwa",
                SessionId="0",
                RequestTime="2019-10-10 00:00:00.555",
                ServiceCode="CCORLO01",
                UserInfo=UserInfo(
                    IDNumber="11919992021"
                )
            ),
            Body=Body(
                RequestNumber=request_number,
            ),
        )
    ).dict(exclude_none=True)
