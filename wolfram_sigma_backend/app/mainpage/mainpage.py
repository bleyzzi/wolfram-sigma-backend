from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

def get_mainpage_router():
    return router

class EquationData(BaseModel):
    equation: str
    args: List[float]

@router.post("/post_equation")
async def evaluate_expression(data: EquationData):
    try:
        result = eval(data.expression.format(*data.args))
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error evaluating equation: {str(e)}")
    
