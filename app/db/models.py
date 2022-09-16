from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer, default=True)

    games = relationship("Game", back_populates="user")


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    users_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="games")
