from typing import List

from pydantic import BaseModel


class EquationSchema(BaseModel):
    equation: str
    args: List[float]
