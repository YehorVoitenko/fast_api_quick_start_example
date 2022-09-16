from .db import models, crud
from .schemas import schemas
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/get/me", response_model=schemas.User)
def get_current_user(db: Session = Depends(get_db)):
    db_user = crud.get_last_user(db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/create/{user_id}/game/", response_model=schemas.Game)
def create_game_for_user(
    user_id: int, game: schemas.GameCreate, db: Session = Depends(get_db)
):
    return crud.create_user_game(db=db, game=game, user_id=user_id)


@app.get("/get/games/", response_model=list[schemas.Game])
def read_games_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = crud.get_games_list(db, skip=skip, limit=limit)
    return games
