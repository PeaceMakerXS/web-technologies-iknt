from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker

from .settings import get_db_url

DATABASE_URL = get_db_url()
engine = create_engine(DATABASE_URL, echo=True)
session_local = sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    __abstract__ = True

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}'
