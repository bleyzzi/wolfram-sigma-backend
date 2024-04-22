from wolfram_sigma_backend.app.persistence.unit_of_work.interface_uow import IUnitOfWork


class UnitOfWork(IUnitOfWork):
    def __init__(self, session_maker):
        super().__init__()
        self.session_factory = session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()