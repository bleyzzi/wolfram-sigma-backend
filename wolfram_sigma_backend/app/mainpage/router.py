from typing import Dict, Any

from fastapi import HTTPException
from fastapi import APIRouter

from wolfram_sigma_backend.app.mainpage.schemas import EquationData

router = APIRouter()


@router.post("/post_equation")
async def evaluate_expression(data: EquationData) -> Dict[str, Any]:
    try:
        result = eval(data.equation.format(*data.args))
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error evaluating equation: {str(e)}")
