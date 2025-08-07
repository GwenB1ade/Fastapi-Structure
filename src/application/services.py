from src.domain.repositories import IUserRepository


class UserService:
    def __init__(self, repo: IUserRepository):
        self.repo = repo
