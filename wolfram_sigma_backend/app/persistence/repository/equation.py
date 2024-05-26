from wolfram_sigma_backend.app.models.main_page_models import Equation
from wolfram_sigma_backend.app.persistence.repository.sql_alchemy_repository import (
    SQLAlchemyRepository,
)


class EquationRepository(SQLAlchemyRepository):
    model = Equation
