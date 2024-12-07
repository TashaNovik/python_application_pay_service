from pydantic import BaseModel
from decimal import Decimal

class PaymentSchema(BaseModel):
    user_id: str
    payment_id: str
    amount: Decimal
    email: str | None
    type: str | None
    company_id: int

class Config:
    pass