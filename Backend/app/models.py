from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=True, default=username)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    sender = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    receiver = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable = False)
    createdat = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

