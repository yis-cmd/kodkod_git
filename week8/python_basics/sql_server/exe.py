import asyncio

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import select, Select, String

from fastapi import FastAPI, Depends

DB_URL = "mysql+aiomysql://python:123456@localhost/users"
async_engine = create_async_engine(DB_URL)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)

async def get_session():
    async with async_session() as session:
        yield session

class Base(DeclarativeBase):
    def __str__(self) -> str:
        columns = {c.name:getattr(self, c.name) for c in self.__table__.columns}
        return f"{columns}"
    
class Details(Base):
    __tablename__ = "details"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(50))
    phone_number:Mapped[str] = mapped_column(String(12))

app = FastAPI()

async def get_details(user_id:int, session:AsyncSession = Depends(get_session)):
    stmt = select(Details).where(getattr(Details, "id") == user_id)
    await session.execute(stmt)