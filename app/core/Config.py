from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')
    dbHost:str
    dbUsername:str
    dbPassword:str
    dbDatabase:str
    logKey:str

settings = Settings()
