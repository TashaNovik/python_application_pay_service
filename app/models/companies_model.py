from sqlalchemy import Column, Integer, String
from app.db import Base


class Company(Base):
    __tablename__ = "companies"

    name = Column(String)
    company_id = Column(Integer, primary_key=True, autoincrement=True)
