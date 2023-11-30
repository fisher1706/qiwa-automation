from data.dedicated.models.user import User
from src.api.payloads.ibm.getestablishmentinformation import (
    EstablishmentInformation,
    GetEstablishmentInformationPayload,
    GetEstablishmentInformationRq,
)
from src.api.payloads.ibm.header import Header


def establishment_information_payload(user: User):
    return GetEstablishmentInformationPayload(
        GetEstablishmentInformationRq=GetEstablishmentInformationRq(
            Header=Header(
                TransactionId="0",
                ChannelId="Qiwa",
                SessionId="0",
                RequestTime="2019-10-10 00:00:00.555",
                MWRequestTime="2019-10-10 00:00:00.555",
                ServiceCode="GEI00001",
                DebugFlag="1",
            ),
            Body=EstablishmentInformation(
                LaborOfficeId=user.labor_office_id,
                EstablishmentSequanceNumber=user.sequence_number,
            ),
        )
    ).dict()
