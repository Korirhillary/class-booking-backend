from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from database import get_db
from sqlalchemy.orm import Session
from models import Lecturehall, User, Booklecturehall
from schemas import LecturehallSchema, UserSchema

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"message": "Welcome to my first API"}

@app.get('/lecturehalls')
def lecturehalls(db: Session = Depends(get_db)):
    lecturehalls = db.query(Lecturehall).all()
    return lecturehalls

@app.get('/lecturehalls/{room_id}')
def lecturehall(room_id: int, db: Session = Depends(get_db)):
    lecturehall = db.query(Lecturehall).filter(Lecturehall.id == room_id).first()
    return lecturehall

@app.post('/lecturehalls')
def set_lecturehall(lecturehall: LecturehallSchema, db: Session = Depends(get_db)):
    new_lecturehall = Lecturehall(**lecturehall.id())
    db.add(new_lecturehall)
    db.commit()
    db.refresh(new_lecturehall)
    return {"message": "Lecturehall set successfully"}

@app.post('/booklecturehall')
def book_lecturehall(book_lecturehall: UserSchema, db: Session = Depends(get_db)):
    user_instance = User(**book_lecturehall)
    db.add(user_instance)
    db.commit()
    db.refresh(user_instance)

    new_book_lecturehall = Booklecturehall(
        book_lecturehall_date=book_lecturehall.book_lecturehall_date,
        user_id=user_instance.id,
        lecturehall_id=book_lecturehall.lecturehall_id
    )
    db.add(new_book_lecturehall)
    db.commit()
    db.refresh(new_book_lecturehall)

    return {"message": "Lecturehall booked successfully"}

@app.get('/book-room')
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.patch('/lecturehalls/{room_id}')
def update_lecturehall(room_id: int):
    return {"message": f"Lecturehall {room_id} booked successfully"}

@app.delete('/lecturehalls/{lecturehall_id}')
def delete_lecturehall(lecturehall_id: int):
    return {"message": f"Lecturehall {lecturehall_id} deleted successfully"}
