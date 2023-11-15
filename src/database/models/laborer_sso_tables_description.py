# disabled because it is DB table descriptions
# pylint: disable = too-few-public-methods
from datetime import datetime, timezone

from sqlalchemy import (
    JSON,
    VARCHAR,
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Integer,
    Text,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AccountsEmails(Base):
    __tablename__ = "accounts_emails"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    account_id = Column("account_id", Integer, nullable=False)
    email_id = Column("email_id", Integer, nullable=False)
    confirmation_sent_at = Column("confirmation_sent_at", DateTime(timezone=False))
    confirmation_token = Column("confirmation_token", Text)
    state = Column("state", Text, nullable=False)
    enabled = Column("enabled", Boolean, nullable=False)
    enabled_at = Column("enabled_at", DateTime(timezone=False))
    disabled_at = Column("disabled_at", DateTime(timezone=False))
    created_at = Column("created_at", DateTime(timezone=False))
    updated_at = Column("updated_at", DateTime(timezone=False))


class OauthApplications(Base):
    __tablename__ = "oauth_applications"

    id = Column("id", Integer, primary_key=True, nullable=False)
    account_id = Column("account_id", BigInteger, nullable=False)
    name = Column("name", Text, nullable=False)
    description = Column("description", Text, nullable=False)
    homepage_url = Column("homepage_url", Text, nullable=False)
    redirect_uri = Column("redirect_uri", Text, nullable=False)
    client_id = Column("client_id", Text, nullable=False)
    client_secret = Column("client_secret", Text, nullable=False)
    scopes = Column("scopes", Text, nullable=False)
    token_endpoint_auth_method = Column("token_endpoint_auth_method", Text)
    grant_types = Column("grant_types", Text)
    response_types = Column("response_types", Text)
    client_uri = Column("client_uri", Text)
    logo_uri = Column("logo_uri", Text)
    tos_uri = Column("tos_uri", Text)
    policy_uri = Column("policy_uri", Text)
    jwks_uri = Column("jwks_uri", Text)
    jwks = Column("jwks", Text)
    contacts = Column("contacts", Text)
    software_id = Column("software_id", Text)
    permissions = Column("permissions", Text, nullable=False)
    created_at = Column("created_at", DateTime(timezone=False))
    updated_at = Column("updated_at", DateTime(timezone=False))
    main = Column("main", Boolean, nullable=False)


class OauthGrants(Base):
    __tablename__ = "oauth_grants"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    account_id = Column("account_id", Integer, nullable=False)
    oauth_application_id = Column("oauth_application_id", nullable=False)
    type = Column("type", Text, nullable=False)
    code = Column("code", Text)
    token_hash = Column("token_hash", Text)
    refresh_token_hash = Column("refresh_token_hash", Text)
    expires_in = Column("expires_in", DateTime(timezone=False), nullable=False)
    redirect_uri = Column("redirect_uri", Text)
    scopes = Column("scopes", Text, nullable=False)
    access_type = Column("access_type", Text, nullable=False)
    nonce = Column("nonce", Text)
    session_key_hash = Column("session_key_hash", Text)
    code_challenge = Column("code_challenge", Text)
    code_challenge_method = Column("code_challenge_method", Text)


class AccountsPhone(Base):
    __tablename__ = "accounts_phones"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    account_id = Column("account_id", Integer, nullable=False)
    phone_id = Column("phone_id", Integer, nullable=False)
    state = Column("state", Text, nullable=False)
    enabled = Column("enabled", Boolean, nullable=False, default=False)
    enabled_at = Column("enabled_at", DateTime(timezone=False))
    disabled_at = Column("disabled_at", DateTime(timezone=False))
    created_at = Column("created_at", DateTime(timezone=False))
    updated_at = Column("updated_at", DateTime(timezone=False))


class AccountLockouts(Base):
    __tablename__ = "account_lockouts"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    key = Column("key", Text, nullable=False)
    deadline = Column("deadline", DateTime(timezone=False), nullable=False)
    last_sent = Column("last_sent", DateTime(timezone=False))


class Accounts(Base):
    __tablename__ = "accounts"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    status_id = Column("status_id", Integer, nullable=False)
    national_id = Column("national_id", VARCHAR(20))
    iqama_id = Column("iqama_id", VARCHAR(20))
    border_number = Column("border_number", VARCHAR(20))
    gregorian_birth_date = Column("gregorian_birth_date", Date)
    hijri_birth_date = Column("hijri_birth_date", Text)
    theme = Column("theme", Text, nullable=False)
    language = Column("language", VARCHAR(3))
    admin = Column("admin", Boolean, nullable=False)
    created_at = Column("created_at", DateTime(timezone=False))
    updated_at = Column("updated_at", DateTime(timezone=False))


class Emails(Base):
    __tablename__ = "emails"

    id = Column("id", Integer, primary_key=True, nullable=False)
    value = Column("value", Text, nullable=False)
    created_at = Column("created_at", DateTime(timezone=False))
    updated_at = Column("updated_at", DateTime(timezone=False))


class Phones(Base):
    __tablename__ = "phones"

    id = Column("id", Integer, primary_key=True, nullable=False)
    value = Column("value", Text, nullable=False)
    created_at = Column("created_at", DateTime(timezone=False))
    updated_at = Column("updated_at", DateTime(timezone=False))


class Logins(Base):
    __tablename__ = "logins"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    account_id = Column("account_id", BigInteger)
    value = Column("value", Text, nullable=False)
    created_at = Column("created_at", DateTime(timezone=False))
    updated_at = Column("updated_at", DateTime(timezone=False))


class AccountPasswordHashes(Base):
    __tablename__ = "account_password_hashes"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    password_hash = Column("password_hash", Text, nullable=False)


class AccountPreviousPasswordHashes(Base):
    __tablename__ = "account_previous_password_hashes"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    account_id = Column("account_id", BigInteger)
    password_hash = Column("password_hash", Text, nullable=False)
    metadata_column = Column("metadata", JSON)


class AccountAuthenticationAuditLogs(Base):
    __tablename__ = "account_authentication_audit_logs"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    account_id = Column("account_id", BigInteger, nullable=False)
    at = Column("at", DateTime(timezone=False), nullable=False)
    message = Column("message", Text, nullable=False)
    metadata_column = Column("metadata", JSON)


class AccountActiveSessionKeys(Base):
    __tablename__ = "account_active_session_keys"

    account_id = Column("account_id", BigInteger, primary_key=True, nullable=False)
    session_id = Column("session_id", Text, primary_key=True, nullable=False)
    created_at = Column("created_at", DateTime(timezone=False), nullable=False)
    last_use = Column("last_use", DateTime(timezone=False), nullable=False)


class Activities(Base):
    __tablename__ = "activities"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    entity_type = Column("entity_type", Text, nullable=False)
    entity_value = Column("entity_value", Text, nullable=False)
    counter = Column("counter", Integer, nullable=False)
    at = Column("at", DateTime(timezone=False), nullable=False)
    name = Column("name", Text, nullable=False)


class SecurityQuestions(Base):
    __tablename__ = "security_questions"

    id = Column("id", Integer, primary_key=True, nullable=False)
    account_id = Column("account_id", Integer, nullable=False)
    mother_dob = Column("mother_dob", Text)
    mother_name = Column("mother_name", Text)
    passport_number = Column("passport_number", Text)
    school_graduation = Column("school_graduation", Text)
    school_name = Column("school_name", Text)
    created_at = Column("created_at", DateTime(timezone=False))
    updated_at = Column("updated_at", DateTime(timezone=False))


class AccountLoginFailures(Base):
    __tablename__ = "account_login_failures"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    number = Column("number", Integer, nullable=False)


class AccountPasswordResetKeys(Base):
    __tablename__ = "account_password_reset_keys"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    key = Column("key", Text, nullable=False)
    deadline = Column(
        "deadline", DateTime(timezone=False), nullable=False, default=datetime.now(tz=timezone.utc)
    )
    last_sent = Column(
        "last_sent", DateTime(timezone=False), nullable=False, default=datetime.now()
    )


class ResetPasswordActivityTrails(Base):
    __tablename__ = "reset_password_activity_trails"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    personal_number = Column("personal_number", Text)
    send_otp_counter = Column("send_otp_counter", Integer, default=0)
    wrong_otp_entered_attempts = Column("wrong_otp_entered_attempts", Integer, default=0)
    last_sent_otp_time = Column("last_sent_otp_time", DateTime(timezone=False))
    success_reset_password_counter = Column("success_reset_password_counter", Integer)
    success_reset_password_first_time = Column(
        "success_reset_password_first_time", DateTime(timezone=False)
    )
    send_otp_locked_until = Column("send_otp_locked_until", DateTime(timezone=False))
    wrong_otp_locked_until = Column("wrong_otp_locked_until", DateTime(timezone=False))
    created_at = Column("created_at", DateTime(timezone=False))
    updated_at = Column("updated_at", DateTime(timezone=False))
