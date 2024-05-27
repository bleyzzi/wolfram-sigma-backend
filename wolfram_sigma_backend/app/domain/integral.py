from pydantic import BaseModel


class IntegralSchema(BaseModel):
    equation: str
