from sqlalchemy import Column, Float, String, Text, Unicode, BigInteger

from core.db import Base
from core.db.mixins import TimestampMixin


class Shop(Base, TimestampMixin):
    __tablename__ = "shops"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    name = Column(Unicode(200), nullable=True, default=None)
    logo = Column(String, nullable=True, default=None)
    sliders = Column(Text, nullable=True)
    phone = Column(String, nullable=True, default=None)
    address = Column(Unicode(300), nullable=True, default=None)
    country = Column(Unicode(30), nullable=True)
    city = Column(Unicode(30), nullable=True)
    postal_code = Column(Unicode(20), nullable=True)
    facebook = Column(String, nullable=True, default=None)
    google = Column(String, nullable=True, default=None)
    twitter = Column(String, nullable=True, default=None)
    youtube = Column(String, nullable=True, default=None)
    slug = Column(String, nullable=True, default=None)
    meta_title = Column(String, nullable=True, default=None)
    meta_description = Column(Text, nullable=True, default=None)
    pick_up_point_id = Column(Text, nullable=True, default=None)
    shipping_cost = Column(Float(precision=2), nullable=False, default=0.00)
