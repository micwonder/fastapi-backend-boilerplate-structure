from sqlalchemy import Column, Unicode, BigInteger, Text, TIMESTAMP

from core.db import Base
from core.db.mixins import TimestampMixin


class BusinessSetting(Base, TimestampMixin):
    __tablename__ = "business_settings"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    type = Column(Unicode(30), nullable=False)
    value = Column(Text, nullable=True)
    lang = Column(Unicode(30), nullable=True, default=None)

