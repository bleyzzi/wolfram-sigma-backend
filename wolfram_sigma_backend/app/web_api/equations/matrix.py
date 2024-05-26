from fastapi import HTTPException

from wolfram_sigma_backend.app.domain.equation import EquationSchema, EquationsSchemas
from wolfram_sigma_backend.app.domain.matrix import MatrixSchema
from wolfram_sigma_backend.app.infrastructure.math.matrix_processor import (
    MatrixProcessorFromCLib,
)
from wolfram_sigma_backend.app.persistence.service.equation import EquationService
from wolfram_sigma_backend.app.web_api.equations.router import equations_router


@equations_router.post("/matrix_multiplication")
async def matrix_multiplication(m1: MatrixSchema, m2: MatrixSchema, num_threads: int = 1) -> MatrixSchema:
    try:
        res = MatrixProcessorFromCLib().matrix_multiplication(m1.values, m2.values, num_threads)
        await EquationService.add_equation(
            EquationSchema(expression=f"{str(m1.values)} X {str(m2.values)}", result=str(res), params_id=num_threads)
        )
        return MatrixSchema(values=res)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"{e}")


@equations_router.post("/matrix_determinant")
async def matrix_determinant(m: MatrixSchema, num_threads: int = 1) -> float:
    try:
        res = MatrixProcessorFromCLib().matrix_determinate(m.values, num_threads)
        await EquationService.add_equation(
            EquationSchema(expression=f"DET({str(m.values)})", result=str(res), params_id=num_threads)
        )
        return res
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"{e}")


@equations_router.post("/inverse_matrix")
async def inverse_matrix(m: MatrixSchema) -> MatrixSchema:
    try:
        res = MatrixProcessorFromCLib().inverse_matrix(m.values)
        await EquationService.add_equation(
            EquationSchema(expression=f"INVERSE({str(m.values)})", result=str(res), params_id=1)
        )
        return MatrixSchema(values=res)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"{e}")


@equations_router.get("/all_equations")
async def get_all_equations() -> EquationsSchemas:
    lst = await EquationService.get_equations()
    return EquationsSchemas(equations=lst)
