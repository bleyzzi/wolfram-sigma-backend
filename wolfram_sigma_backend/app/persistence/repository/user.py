from wolfram_sigma_backend.app.models.auth_models import User
from wolfram_sigma_backend.app.persistence.repository.sql_alchemy_repository import (
    SQLAlchemyRepository,
)


class UserRepository(SQLAlchemyRepository):
    model = User
