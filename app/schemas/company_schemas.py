from pydantic import BaseModel, ConfigDict


class CompanySchema(BaseModel):
    name: str
    model_config = ConfigDict(from_attributes=True)
