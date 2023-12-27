from dataclasses import dataclass


@dataclass
class TableFilters:
    VISIBLE_FILTERS = {
        "payment_status": {
            "filter_header_text": "Payment status",
            "related_column": "Payment status",
            "filter_options": [
                "Paid",
                "Unpaid"
                # "Canceled" Not available in test data
            ],
        },
        "objection": {
            "filter_header_text": "Objection",
            "related_column": "Objection ID",
            "filter_options": ["Objected", "Not objected"],
        },
        "date_of_violation": {
            "filter_header_text": "Date of Violation",
            "related_column": "Violation date",
            "filter_options": ["Start date", "End date"],
        },
        "date_of_blocking_the_service": {
            "filter_header_text": "Date of blocking the service",
            "related_column": "Due date",
            "filter_options": ["Start date", "End date"],
        },
    }
    START_DATE_FOR_FILTER = "02/01/2023"
    END_DATE_FOR_FILTER = "02/01/2023"


@dataclass
class UserWithEstablishmentViolations:
    ID = "1026566289"
    ESTABLISHMENT_SEQUENCE = 101
    CANNOT_OBJECT_VIOLATION_ID = "V-4162"
    AVAILABLE_OBJECT_VIOLATION_ID = "V-4631"


@dataclass
class SortingData:
    SORT_DICT = {
        "Violation ID - highest no.": {
            "column_name": "Violation ID",
            "requires_sanitization": False,
            "is_date": False,
            "DSC": True,
        },
        "Violation ID - lowest no.": {
            "column_name": "Violation ID",
            "requires_sanitization": False,
            "is_date": False,
            "DSC": False,
        },
        "Violation date - newest first": {
            "column_name": "Violation date",
            "requires_sanitization": False,
            "is_date": True,
            "DSC": True,
        },
        "Violation date - oldest first": {
            "column_name": "Violation date",
            "requires_sanitization": False,
            "is_date": True,
            "DSC": False,
        },
        "Due date - closest first": {
            "column_name": "Due date",
            "requires_sanitization": False,
            "is_date": True,
            "DSC": True,
        },
        "Due date - latest first": {
            "column_name": "Due date",
            "requires_sanitization": False,
            "is_date": True,
            "DSC": False,
        },
        "Fee - highest first": {
            "column_name": "Fee",
            "requires_sanitization": True,
            "is_date": False,
            "DSC": True,
        },
        "Fee - lowest first": {
            "column_name": "Fee",
            "requires_sanitization": True,
            "is_date": False,
            "DSC": False,
        },
    }


@dataclass
class TableColumns:
    VIOLATION_ID = "Violation ID"
    OBJECTION_ID = "Objection ID"
    DUE_DATE = "Due date"
    FEE = "Fee"
    SADAD_NUMBER = "SADAD number"
    VIOLATION_DATE = "Violation date"
    PAYMENT_STATUS = "Payment status"
    ACTIONS = "Actions"
    COLUMNS = {
        "Violation ID": {"pattern": r"^V-\d+$"},
        "Objection ID": {"pattern": r"^O-\d+$"},
        "Due date": {"pattern": r"^\d{2}/\d{2}/\d{4}$"},
        "Fee": {"pattern": r"^\d+\sSAR$"},
        "SADAD number": {"pattern": r"^\d+$"},
        "Violation date": {"pattern": r"^\d{2}/\d{2}/\d{4}$"},
        "Payment status": {"pattern": r"^(Paid|Unpaid)$"},
        "Actions": {"pattern": r"^View Details$"},
    }


@dataclass
class PageText:
    TITLE = "Establishment Violations"
    GENERAL_INFO_ONE = (
        "The Establishment Violations service allows employers to review details and object "
        "to violations imposed by government parties."
    )
    GENERAL_INFO_TWO = (
        "Objection to the violation is possible within 60 days from the violation date."
    )


@dataclass
class ViolationDetailsPageText:
    CANNOT_OBJECT_VIOLATION_HEADER = "You cannot object to this violation anymore"
    CANNOT_OBJECT_VIOLATION_BODY = (
        "Filing an objection is possible within 60 days from the violation date."
        " After this deadline, the objection will not be possible, and fee must be paid."
    )
    KEYS = {
        "Violation ID": {"pattern": r"^V-\d+$"},
        "Objection ID": {"pattern": r"^O-\d+$"},
        "Due date": {"pattern": r"^\d{2}/\d{2}/\d{4}$"},
        "Fee": {"pattern": r"^\d+\sSAR$"},
        "SADAD number": {"pattern": r"^\d+$"},
        "Violation date": {"pattern": r"^\d{2}/\d{2}/\d{4}$"},
        "Payment status": {"pattern": r"^(Paid|Unpaid)$"},
    }
    OBJECTION_KEYS = {
        "Objection ID": {"pattern": r"^O-\d+$"},
        "Objection date": {"pattern": r"^\d{2}/\d{2}/\d{4}$"},
    }


@dataclass
class PaginationOptions:
    OPTIONS = [5, 10, 30, 50]
