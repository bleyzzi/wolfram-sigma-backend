import datetime

from pydantic import BaseModel


class EquationSchema(BaseModel):
    expression: str
    result: str
    params_id: int

    class Config:
        from_attributes = True


class EquationGetSchema(BaseModel):
    id: int
    expression: str
    result: str
    params_id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True


class EquationsSchemas(BaseModel):
    equations: list[EquationGetSchema]
