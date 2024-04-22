from typing import Annotated

from fastapi import Depends

from wolfram_sigma_backend.app.persistence.unit_of_work.interface_uow import IUnitOfWork
from wolfram_sigma_backend.app.persistence.unit_of_work.uow import UnitOfWork

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
