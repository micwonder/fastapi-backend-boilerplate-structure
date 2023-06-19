from sqlalchemy import Column, Float, Integer, String, Text, Unicode, BigInteger

from core.db import Base
from core.db.mixins import TimestampMixin


class Seller(Base, TimestampMixin):
    __tablename__ = "sellers"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    verification_status = Column(Integer, nullable=False, default=0)
    verification_info = Column(Text, nullable=True)
    cash_on_delivery_status = Column(Integer, nullable=False, default=0)
    admin_to_pay = Column(Float(precision=2), nullable=False, default=0.00)
    bank_name = Column(String, nullable=True, default=None)
    bank_acc_name = Column(Unicode(200), nullable=True, default=None)
    bank_acc_no = Column(Unicode(50), nullable=True, default=None)
    bank_routing_no = Column(Integer, nullable=True)
    bank_payment_status = Column(Integer, nullable=False, default=0)

