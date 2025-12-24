from fastapi import FastAPI, Depends
from sqlmodel import Session
from app.database import get_session
from app.models import User

app = FastAPI()


@app.post("/users")
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
