from sqlalchemy import Column, Numeric, String, UUID, Integer, ForeignKey

from app.db import Base
from app.models.base_model import BaseModel
from sqlalchemy.orm import relationship


class Payment(Base, BaseModel):
    __tablename__ = "payments"

    user_id = Column(String, nullable=False)
    payment_id = Column(String, nullable=False, unique=True)
    # Все, что касается платежа должно иметь тип Decimal. Внутри Postgres это Numeric
    amount = Column(Numeric(10, 2), nullable=False)
    email = Column(String)
    type = Column(String(30), nullable=False)
    payment_status = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey("companies.company_id"), nullable=False)
    # вариант с relationship
    #company_id = relationship("Company", back_populates="payments")

    # Как будет выглядеть строковое представление объекта Payment(аналог toString в Java)
    def __repr__(self):
        return (
            f"Payment(user_id={self.user_id!r}, "
            f"payment_id={self.payment_id!r}, "
            f"amount={self.amount!r}, "
            f"email={self.email!r}, "
            f"type={self.type!r}, "
            f"payment_status={self.payment_status!r})"
        )

    def __str__(self):
        return (
            f"Payment(user_id={self.user_id!r}, "
            f"payment_id={self.payment_id!r}, "
            f"amount={self.amount!r}, "
            f"email={self.email!r}, "
            f"type={self.type!r}, "
            f"payment_status={self.payment_status!r})"
        )
