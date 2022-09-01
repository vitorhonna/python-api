from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    email: str
    user_id: str


@app.get("/users/all")
def all_users():
    return {"message": 'all users'}


@app.get("/users/{user_id}")
def get_user(user_id: str | None = None):
    if not user_id:
        return {"message": 'Please provide an user ID: /users?id=USER_ID'}

    return {'user': f'specific user, id = {user_id}'}


@app.post("/users/add")
def add_user(user: User):
    pass


@app.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    return {"user_name": user.name, "user_id": user_id}
