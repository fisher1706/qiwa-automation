import enum


class RequestStatus(enum.Enum):
    PENDING = "0"
    APPROVED_BY_NIC = "1"
    REJECTED_BY_NIC = "2"
    NIC_FAILURE = "3"
    AUTO_TERMINATED = "4"
