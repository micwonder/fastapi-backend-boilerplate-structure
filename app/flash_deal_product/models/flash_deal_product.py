from sqlalchemy import Column, TIMESTAMP, Float, String, BigInteger

from core.db import Base
from core.db.mixins import TimestampMixin


class FlashDealProduct(Base, TimestampMixin):
    __tablename__ = "flash_deal_products"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    flash_deal_id = Column(BigInteger, nullable=False)
    product_id = Column(BigInteger, nullable=False)
    discount = Column(Float(precision=2), nullable=False)
    discount_type = Column(String(10), nullable=True, default=None)
