# src/config/config.py
class Config:
    SQLALCHEMY_DATABASE_URI = (
        'postgresql://admin:admin@localhost:5432/postgres'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
