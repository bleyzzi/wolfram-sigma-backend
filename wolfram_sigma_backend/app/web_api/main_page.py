from typing import Any, Dict

from fastapi import APIRouter, HTTPException

from wolfram_sigma_backend.app.domain.main_page import EquationSchema

main_page_router = APIRouter()


@main_page_router.post("/post_equation")
async def evaluate_expression(data: EquationSchema) -> Dict[str, Any]:
    try:
        result = eval(data.equation.format(*data.args))
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error evaluating equation: {str(e)}")
