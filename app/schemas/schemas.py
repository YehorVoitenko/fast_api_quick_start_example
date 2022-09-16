from fastapi import Query
from pydantic import BaseModel, EmailStr


class GameBase(BaseModel):
    name: str


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int
    users_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int = Query(gt=0, lt=100)


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    games: list[Game] = []

    class Config:
        orm_mode = True
