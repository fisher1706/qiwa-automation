from sqlalchemy import BigInteger, Column, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BalanceRequests(Base):  # pylint: disable=too-few-public-methods
    __tablename__ = "balance_requests"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    payment_id = Column("payment_id", Text, nullable=False)
    status = Column("status", Text, nullable=False)
    reference_number = Column("reference_number", Text, nullable=False)
