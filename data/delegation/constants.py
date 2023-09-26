from dataclasses import dataclass


@dataclass
class DelegationStatus:
    ACTIVE = "ACTIVE"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"
    PENDING = "PENDING"


@dataclass
class DelegationAction:
    PREVIEW_LETTER = "Preview letter"
    REVOKE = "Revoke"
    VIEW_DETAILS = "View details"


@dataclass
class DelegationDetailsData:
    PENDING_REQUEST = "Pending Approval"
    RESEND_ACTION = "Resend approval request"
