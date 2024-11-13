from app.repositories import company_repo


class CompanyService:
    def __init__(self):
        self.company_repo = company_repo

    async def create_new_company(self, body: RequestSchema) -> None:
        try:
            await self.company_repo(body)
        except:
            pass




