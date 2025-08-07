from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_PORT: int
    DB_HOST: str

    RABBIT_USER: str
    RABBIT_PASS: str
    RABBIT_PORT: int
    RABBIT_HOST: str

    REDIS_PORT: int
    REDIS_HOST: str
    REDIS_DB: int

    JWT_SECRET: str
    JWT_ALGORITHM: str
    SESSION_SECRET: str

    API_HOST: str
    API_PORT: int

    @property
    def database_url(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def async_database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def redis_url(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/1"

    @property
    def rabbitmq_url(self):
        return f"amqp://{self.RABBIT_USER}:{self.RABBIT_PASS}@{self.RABBIT_HOST}:{self.RABBIT_PORT}/"

    @property
    def jwt_secret(self):
        return self.JWT_SECRET

    @property
    def origins(self):
        return [
            f"http://{self.API_HOST}:{self.API_PORT}",
        ]

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # pyright: ignore[reportCallIssue]
