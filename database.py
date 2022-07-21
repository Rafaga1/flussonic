# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import as_declarative

# DATABASE_URL_ASYNC = "sqlite+aiosqlite:///./pets.db"
# engine = create_async_engine(DATABASE_URL_ASYNC)
# async_session = sessionmaker(engine, class_=AsyncSession)
# session = async_session()

DATABASE_URL = "sqlite:///./pets.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base(bind=engine)
