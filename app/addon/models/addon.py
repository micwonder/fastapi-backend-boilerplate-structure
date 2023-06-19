from sqlalchemy import Column, TIMESTAMP, Text, Unicode, BigInteger, Integer

from core.db import Base
from core.db.mixins import TimestampMixin


class Addon(Base, TimestampMixin):
    __tablename__ = "addons"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(Unicode(200), nullable=True, default=None)
    unique_identifier = Column(Unicode(200), nullable=True, default=None)
    version = Column(Unicode(200), nullable=True, default=None)
    activated = Column(Integer, default=1)
    image = Column(Text, nullable=True, default=None)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
