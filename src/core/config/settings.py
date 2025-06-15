from decouple import config



class Config:

    sql_database_url = config("DATABASE_URL")

    if sql_database_url and sql_database_url.startswith("postgres://"):
        sql_database_url = sql_database_url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = sql_database_url



class DevelopmentConfig(Config):
    ...

class ProductionConfig(Config):
    ...

class TestingConfig(Config):
    ...

config_ = {"development": DevelopmentConfig, "production": ProductionConfig, "testing":TestingConfig }