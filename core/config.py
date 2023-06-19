import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    WRITER_DB_URL: str = f"mysql+aiomysql://merchant2easyric_root:easyriceasyric@localhost:3306/merchant2easyric_easyric"
    READER_DB_URL: str = f"mysql+aiomysql://merchant2easyric_root:easyriceasyric@localhost:3306/merchant2easyric_easyric"
    JWT_SECRET_KEY: str = "easyric"
    JWT_ALGORITHM: str = "HS256"
    SENTRY_SDN: str = None
    CELERY_BROKER_URL: str = None
    CELERY_BACKEND_URL: str = None
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


class DevelopmentConfig(Config):
    WRITER_DB_URL: str = f"mysql+aiomysql://merchant2easyric_root:easyriceasyric@localhost:3306/merchant2easyric_easyric"
    READER_DB_URL: str = f"mysql+aiomysql://merchant2easyric_root:easyriceasyric@localhost:3306/merchant2easyric_easyric"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379


class LocalConfig(Config):
    WRITER_DB_URL: str = f"mysql+aiomysql://merchant2easyric_root:easyriceasyric@localhost:3306/merchant2easyric_easyric"
    READER_DB_URL: str = f"mysql+aiomysql://merchant2easyric_root:easyriceasyric@localhost:3306/merchant2easyric_easyric"


class ProductionConfig(Config):
    DEBUG: str = False
    WRITER_DB_URL: str = f"mysql+aiomysql://root:123456@localhost:3306/easyric"
    READER_DB_URL: str = f"mysql+aiomysql://root:123456@localhost:3306/easyric"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type["prod"]


config: Config = get_config()
