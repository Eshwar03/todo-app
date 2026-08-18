from database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,ForeignKey
from datetime import datetime

class User(Base):
    __tablename__="user"
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    email:Mapped[str]=mapped_column(unique=True)
    name:Mapped[str]=mapped_column(String(100))
    hashed_password:Mapped[str]=mapped_column()
    created_at:Mapped[datetime]=mapped_column(default=datetime.utcnow)

class Todo(Base):
    __tablename__="todo"
    id:Mapped[int]=mapped_column(primary_key=True,unique=True,index=True)
    title:Mapped[str]=mapped_column(String(100))
    description:Mapped[str|None]=mapped_column()
    completed:Mapped[bool]=mapped_column(default=False)
    created_at:Mapped[datetime]=mapped_column(default=datetime.utcnow)
    user_id:Mapped[int]=mapped_column(ForeignKey("user.id"),index=True)


