from sqlalchemy import Column, TIMESTAMP, Text, String, BigInteger, Integer

from core.db import Base
from core.db.mixins import TimestampMixin


class ProductTranslation(Base, TimestampMixin):
    __tablename__ = "product_translations"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    product_id = Column(BigInteger, nullable=False)
    name = Column(String(200), nullable=True, default=None)
    unit = Column(String(20), nullable=True, default=None)
    description = Column(Text, nullable=True)
    lang = Column(String(100), nullable=False)
