from sqlalchemy import Column, TIMESTAMP, String, Float, BigInteger, Integer, Text

from core.db import Base
from core.db.mixins import TimestampMixin


class ProductStock(Base, TimestampMixin):
    __tablename__ = "product_stocks"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    product_id = Column(BigInteger, nullable=False)
    variant = Column(String, nullable=False)
    sku = Column(String, nullable=True, default=None)
    price = Column(Float(precision=2), nullable=False, default=0)
    qty = Column(Integer, nullable=False, default=0)
    image = Column(Text, nullable=True, default=None)
