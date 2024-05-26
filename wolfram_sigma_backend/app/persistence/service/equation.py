from wolfram_sigma_backend.app.domain.equation import EquationGetSchema, EquationSchema
from wolfram_sigma_backend.app.persistence.database_config import get_async_session
from wolfram_sigma_backend.app.persistence.repository.equation import EquationRepository


class EquationService:
    @staticmethod
    async def add_equation(equation: EquationSchema) -> None:
        session = get_async_session()
        equation_dict = equation.model_dump()
        await EquationRepository(await anext(session)).add_one(equation_dict)

    @staticmethod
    async def get_equations():
        session = get_async_session()
        res = await EquationRepository(await anext(session)).find_all()
        return [EquationGetSchema.model_validate(row) for row in res]
