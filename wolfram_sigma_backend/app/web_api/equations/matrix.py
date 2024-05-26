from fastapi import HTTPException

from wolfram_sigma_backend.app.domain.matrix import MatrixSchema
from wolfram_sigma_backend.app.infrastructure.math.matrix_processor import (
    MatrixProcessorFromCLib,
)
from wolfram_sigma_backend.app.web_api.equations.router import equations_router


@equations_router.post("/matrix_multiplication")
def matrix_multiplication(m1: MatrixSchema, m2: MatrixSchema, num_threads: int = 1) -> MatrixSchema:
    try:
        res = MatrixProcessorFromCLib().matrix_multiplication(m1.values, m2.values, num_threads)
        return MatrixSchema(values=res)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"{e}")


@equations_router.post("/matrix_determinant")
def matrix_determinant(m: MatrixSchema, num_threads: int = 1) -> float:
    try:
        res = MatrixProcessorFromCLib().matrix_determinate(m.values, num_threads)
        return res
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"{e}")


@equations_router.post("/inverse_matrix")
def inverse_matrix(m: MatrixSchema) -> MatrixSchema:
    try:
        res = MatrixProcessorFromCLib().inverse_matrix(m.values)
        return MatrixSchema(values=res)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"{e}")
