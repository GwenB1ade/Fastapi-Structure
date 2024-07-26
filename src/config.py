from pydantic_settings import BaseSettings, EnvSettingsSource, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_PORT: int
    DB_HOST: str

    JWT_SECRET: str
    SESSION_SECRET: str
    
    
    @property
    def database_url(self):
        return f'postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    
    
    @property
    def async_database_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    
    
    @property
    def jwt_secret(self):
        return self.JWT_SECRET
    
    
    @property
    def origins(self):
        return [
            "http://localhost:8000",
        ]
    
    model_config = SettingsConfigDict(env_file = '../.env')
    

settings = Settings()