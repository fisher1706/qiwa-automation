# pylint: disable = too-few-public-methods
from sqlalchemy import (
    NVARCHAR,
    VARCHAR,
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Integer,
    Text,
)
from sqlalchemy.dialects.mssql import BIT, UNIQUEIDENTIFIER
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UMSubscriptionPayments(Base):
    __tablename__ = "UM_Subscription_Payments"

    unified_number = Column("FK_UnifiedNumber", BigInteger, primary_key=True, nullable=False)
    personal_number = Column("FK_Idno", VARCHAR(20))
    transaction_id = Column("FK_TransactionId", BigInteger)


class UMPayments(Base):
    __tablename__ = "UM_Payments"

    transaction_id = Column("PK_TransactionId", BigInteger, primary_key=True, nullable=False)
    payment_id = Column("PaymentId", VARCHAR(255))
    payment_reference = Column("PaymentReference", VARCHAR(255))
    payment_status_id = Column("FK_PaymentStatusId", Integer)
    status = Column("Status", Text)
    labor_office_id = Column("FK_LaborOfficeId", BigInteger)
    sequence_number = Column("FK_SequenceNumber", BigInteger)


class UMPrivileges(Base):
    __tablename__ = "UM_Privileges"

    labor_office_id = Column("FK_LaborOfficeId", BigInteger)
    sequence_number = Column("FK_SequenceNumber", BigInteger)
    personal_number = Column("FK_Idno", VARCHAR(20))
    services_id = Column("FK_ServiceId", Integer, primary_key=True, nullable=False)


class UMEstablishmentAccess(Base):
    __tablename__ = "UM_EstablishmentAccess"

    labor_office_id = Column("FK_LaborOfficeId", BigInteger)
    sequence_number = Column("FK_SequenceNumber", BigInteger, primary_key=True, nullable=False)
    personal_number = Column("FK_Idno", VARCHAR(20))
    unified_number = Column("FK_UnifiedNumber", BigInteger)
    has_access = Column("HasAccess", Boolean)


class UMSubscriptions(Base):
    __tablename__ = "UM_Subscriptions"

    unified_number = Column("FK_UnifiedNumber", BigInteger, primary_key=True, nullable=False)
    personal_number = Column("FK_Idno", VARCHAR(20), primary_key=True)
    subscription_status_id = Column("FK_SubscriptionStatusId", Integer)
    expiry_date = Column("ExpireDate", DateTime)
    modified_on = Column("ModifiedOn", DateTime)
    requester_id_number = Column("RequesterIdNo", NVARCHAR(150))


class UserPrivileges(Base):
    __tablename__ = "UserPrivileges"

    id = Column("ID", BigInteger, primary_key=True, nullable=False)
    user_id = Column("User_ID", BigInteger)
    personal_number = Column("ID_NO", VARCHAR(10))
    labor_office_id = Column("Labor_Office_ID", Integer)
    sequence_number = Column("Establishment_Sequence", BigInteger)
    subscription_id = Column("Subscription_ID", BigInteger)
    subscription_status_id = Column("Subscription_Status_ID", Integer)
    privileges_id = Column("Privilege_ID", Integer)
    privileges_status_id = Column("Privilege_Status_ID", Integer)


class UserSubscriptions(Base):
    __tablename__ = "UserSubscriptions"

    id = Column("ID", BigInteger, primary_key=True, nullable=False)
    user_id = Column("User_Id", BigInteger)
    labor_office_id = Column("LaborOfficeId", Integer)
    sequence_number = Column("SequenceNumber", BigInteger)
    status_id = Column("StatusId", Integer)
    subscription_id = Column("SubscriptionId", Integer)
    payment_reference = Column("PaymentReference", VARCHAR(150))
    unified_number = Column("UnifiedNumber", BigInteger)


class Users(Base):
    __tablename__ = "Users"

    id = Column("ID", BigInteger, primary_key=True, nullable=False)
    personal_number = Column("IDNO", VARCHAR(150))


class UMPrivilegesAuditLog(Base):
    __tablename__ = "UM_Privileges_Audit_Log"

    id = Column("ID", BigInteger, primary_key=True, nullable=False)
    personal_number = Column("FK_Idno", NVARCHAR(20))
    sequence_number = Column("FK_SequenceNumber", BigInteger)
    service_id = Column("FK_ServiceId", BigInteger)
    deleted_status = Column("Deleted", BIT)
    log_create_date = Column("LogCreatedOn", DateTime)


class EstablishmentAddress(Base):
    __tablename__ = "EstablishmentAddress"

    id = Column("ID", UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    labor_office = Column("LaborOfficeID", Integer)
    sequence_id = Column("EstablishmentSequenceID", Integer)
    city_ar = Column("City", NVARCHAR(150), nullable=True)
    district_ar = Column("District", NVARCHAR(150), nullable=True)
    street_ar = Column("Street", NVARCHAR(150), nullable=True)
    building_number = Column("BuildingNumber", NVARCHAR(50), nullable=True)
    additional_number = Column("AdditionalNo", Integer, nullable=True)
    city_en = Column("CityEn", NVARCHAR(100), nullable=True)
    district_en = Column("DistrictEn", NVARCHAR(100), nullable=True)
    street_en = Column("StreetEn", NVARCHAR(100), nullable=True)
