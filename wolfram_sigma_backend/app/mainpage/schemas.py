from typing import List

from pydantic import BaseModel


class EquationData(BaseModel):
    equation: str
    args: List[float]
