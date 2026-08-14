from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import DeclarativeBase  
from config import settings


async_engine = create_async_engine(settings.database_url)

async_session = async_sessionmaker(bind=async_engine,class_=AsyncSession,expire_on_commit=False)


async def get_db():
    async with async_session() as session:
        yield session 

class Base(DeclarativeBase):
    pass
