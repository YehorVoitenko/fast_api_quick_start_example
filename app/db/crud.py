from sqlalchemy.orm import Session

from app.db import models
from app.schemas import schemas


def get_last_user(db: Session):
    return db.query(models.User).order_by(-models.User.id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 1, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email,
                          name=user.name,
                          age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_games_list(db: Session, skip: int = 1, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).all()


def create_user_game(db: Session, game: schemas.GameCreate, user_id: int):
    db_game = models.Game(**game.dict(), users_id=user_id)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game
