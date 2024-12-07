
from sqlalchemy import Column, Integer, String
from app.db import Base
from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__ = "companies"

    name = Column(String)
    company_id = Column(Integer, primary_key=True, autoincrement=True)
    # вариант с relationship
    #company_id = relationship("Payment", back_populates="company_id")

