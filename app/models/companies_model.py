from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base
from app.models.base_model import BaseModel


class Company(BaseModel, Base):
    __tablename__ = "companies"

    name = Column(String, unique=True, nullable=False)
    payments = relationship("Payment", back_populates="company")
