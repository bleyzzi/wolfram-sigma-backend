from typing import Any, Dict

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyRepository:
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: Dict[Any, Any]) -> int:
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()

    async def edit_one(self, id: int, data: Dict[Any, Any]) -> int:
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()

    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        return [row for row in res.scalars()]

    async def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = res.scalar_one()
        return res
