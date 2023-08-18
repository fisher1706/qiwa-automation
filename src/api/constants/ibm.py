from enum import Enum


class IBMServices(Enum):
    GET_WORK_PERMIT_REQUESTS = "GetWorkPermitRequests"
    GET_SAUDI_CERTIFICATE = "GetSaudiCertificate"
    VALIDATE_EST_SAUDI_CERTIFICATE = "ValidEstSaudiCertificate"
    SEARCH_CHANGE_OCCUPATION = "SearchChangeOccupation"


IBMServicesResponse = Enum("IBMServicesResponse", [(i.name, i.value + "Rs") for i in IBMServices])
IBMServicesRequest = Enum("IBMServicesRequest", [(i.name, i.value + "Rq") for i in IBMServices])
