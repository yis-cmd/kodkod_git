from pydantic_settings import BaseSettings, SettingsConfigDict

CONFIG_FILE = "config.env"


class Config(BaseSettings):
    host: str | None = None
    port: int | None = None
    user: str | None = None
    password: str | None = None

    model_config = SettingsConfigDict(env_file=CONFIG_FILE, env_prefix="DB_")

config = Config()
