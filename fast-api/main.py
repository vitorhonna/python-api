from fastapi import FastAPI

app = FastAPI()


@app.get('/my-first-api')
def hello():
    return {"message": "Hello world!"}


@app.get("/hello")
def hello_user(name: str | None = None):
    if name is None:
        text = 'Hello!'
    else:
        text = f'Hello, {name}!'
    return {"message": text}


