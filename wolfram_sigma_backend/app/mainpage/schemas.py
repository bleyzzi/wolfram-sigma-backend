from pydantic import BaseModel
from typing import List


class EquationData(BaseModel):
    equation: str
    args: List[float]