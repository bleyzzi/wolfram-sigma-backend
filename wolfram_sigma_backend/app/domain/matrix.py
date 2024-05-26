from typing import List

from pydantic import BaseModel


class MatrixSchema(BaseModel):
    values: List[List[float]]
