# disabled because it is DB table descriptions
# pylint: disable = too-few-public-methods
from sqlalchemy import INTEGER, NVARCHAR, BigInteger, Column, DateTime
from sqlalchemy.dialects.mssql import BIT, UNIQUEIDENTIFIER
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DelegationSms(Base):
    __tablename__ = "SmsLogs"

    id = Column("ID", BigInteger, primary_key=True, nullable=False)
    phone_number = Column("PhoneNumber", NVARCHAR, nullable=False)
    sms_text = Column("SmsText", NVARCHAR, nullable=False)
    created_at = Column("CreatedAt", DateTime(timezone=False), nullable=False)


class DelegationApproveRequests(Base):
    __tablename__ = "DelegationApproveRequests"

    id = Column("ID", UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    delegation_id = Column("DelegationID", nullable=True)
    partner_party_id = Column("PartnerPartyId", NVARCHAR, nullable=False)
    partner_party_id_type = Column("PartnerPartyIdType", NVARCHAR, nullable=False)
    partner_phone_number = Column("PartnerPhoneNumber", NVARCHAR, nullable=False)
    status = Column("Status", NVARCHAR, nullable=False)
    created_at = Column("CreatedAt", DateTime(timezone=False), nullable=True)
    updated_at = Column("UpdatedAt", DateTime(timezone=False), nullable=True)
    reject_reason = Column("RejectReason", NVARCHAR, nullable=True)
    otp_code = Column("OtpCode", NVARCHAR, nullable=True)
    otp_expire_at = Column("OtpExpireAt", DateTime(timezone=False), nullable=True)
    partner_name = Column("PartnerName", NVARCHAR, nullable=True)
    is_available_for_resending = Column("IsAvailableForResending", BIT, nullable=False)
    is_deleted = Column("IsDeleted", BIT, nullable=False)
    delete_at = Column("DeleteAt", DateTime(timezone=False), nullable=True)
    number_of_attempts = Column("NumberOfAttempts", INTEGER, nullable=False)
