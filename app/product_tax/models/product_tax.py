from sqlalchemy import Column, TIMESTAMP, Float, String, BigInteger

from core.db import Base
from core.db.mixins import TimestampMixin


class ProductTax(Base, TimestampMixin):
    __tablename__ = "product_taxes"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    product_id = Column(BigInteger, nullable=False)
    tax_id = Column(BigInteger, nullable=False)
    tax = Column(Float(precision=2), nullable=False)
    tax_type = Column(String(10), nullable=False)
