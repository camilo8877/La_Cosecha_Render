from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    admin_nombre: str
    admin_correo: str
    admin_contrasena: str

    cors_origins: list[str] = ["http://127.0.0.1:5500", "http://localhost:5500"]
    echo_sql: bool = False
    zona_horaria_horas: int = -5

    model_config = SettingsConfigDict(env_file=".env")

    @field_validator("database_url")
    @classmethod
    def usar_driver_psycopg(cls, valor: str) -> str:
        # Render entrega "postgres://" o "postgresql://"; SQLAlchemy necesita el driver psycopg (v3)
        for prefijo in ("postgres://", "postgresql://"):
            if valor.startswith(prefijo):
                return "postgresql+psycopg://" + valor[len(prefijo):]
        return valor


settings = Settings()
