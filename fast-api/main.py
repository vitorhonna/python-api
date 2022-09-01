from fastapi import FastAPI
from pydantic import BaseModel
import jsondatabase
import uuid

app = FastAPI()


class User(BaseModel):
    name: str
    email: str
    score: str


@app.get("/users/all")
def all_users():
    return jsondatabase.all_users()


@app.post("/users/add")
def add_user(user: User):
    jsondatabase.add_user(user.name, user.email, user.score, str(uuid.uuid1()))


@app.get("/users/{user_id}")
def get_user(user_id: str):
    return jsondatabase.get_user(user_id)
