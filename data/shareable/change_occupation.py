import enum


class RequestStatus(enum.Enum):
    DRAFT = 1
    PENDING_EMPLOYER_APPROVAL = 2
    PENDING_LABORER_APPROVAL = 3
    REJECTED_BY_EMPLOYER = 4
    REJECTED_BY_LABORER = 5
    APPROVED_BY_EMPLOYER = 6
    PENDING_NIC_APPROVAL = 7
    APPROVED = 8
    CANCELED_BY_EMPLOYER = 9
    CANCELED_BY_LABORER = 10
    AUTO_CANCELED_DUE_NO_APPROVE_OR_REJECT = 11
    REJECTED_BY_NIC = 12
    ASSOCIATED_WITH_TRANSFER_REQUEST = 13
    AUTO_CANCELED_DUE_NO_NIC_RESPONSE = 14

    @classmethod
    def values(cls) -> list[int]:
        return [e.value for e in cls]