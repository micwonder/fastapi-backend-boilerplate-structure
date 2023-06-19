from sqlalchemy import Column, DateTime, Float, Integer, String, Text, Unicode, BigInteger, TIMESTAMP

from core.db import Base
from core.db.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    referred_by = Column(Integer, nullable=True)
    provider_id = Column(Unicode(50), nullable=True)
    user_type = Column(Unicode(10), nullable=False, default="customer")
    name = Column(Unicode(255), nullable=False, unique=False)
    email = Column(Unicode(255), nullable=False, unique=True)
    email_verified_at = Column(DateTime, nullable=True)
    verification_code = Column(Text, nullable=True)
    new_email_verificiation_code = Column(Text, nullable=True)
    password = Column(Unicode(255), nullable=False)
    remember_token = Column(String, nullable=True)
    device_token = Column(Unicode(256), nullable=True)
    avatar = Column(Unicode(256), nullable=True)
    avatar_original = Column(Unicode(256), nullable=True)
    address = Column(Unicode(300), nullable=True)
    country = Column(Unicode(30), nullable=True)
    city = Column(Unicode(30), nullable=True)
    postal_code = Column(Unicode(20), nullable=True)
    phone = Column(Unicode(20), nullable=True)
    phone_verified_at = Column(TIMESTAMP, nullable=True)
    balance = Column(Float(precision=2), nullable=False, default=0.00)
    banned = Column(Integer, nullable=False, default=0)
    referral_code = Column(Unicode(256), nullable=True)
    customer_package_id = Column(Integer, nullable=True)
    remaining_uploads = Column(Integer, nullable=True)
    otp = Column(String(256), nullable=True)