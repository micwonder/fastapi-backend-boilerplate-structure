from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, BigInteger

from core.db import Base
from core.db.mixins import TimestampMixin


class Seller(Base, TimestampMixin):
    __tablename__ = "pages"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    type = Column(String(50), nullable=False)
    url = Column(String(191), nullable=True, default=0)
    title = Column(String(191), nullable=True)
    slug = Column(String(191), nullable=True, default=0)
    content = Column(Text, nullable=True, default=0.00)
    meta_title = Column(Text, nullable=True, default=None)
    meta_description = Column(String(1000), nullable=True, default=None)
    keywords = Column(String(1000), nullable=True, default=None)
    meta_image = Column(String(191), nullable=True)
    created_at = Column(TIMESTAMP, nullable=True, default=0)
    updated_at = Column(TIMESTAMP, nullable=True, default=0)
