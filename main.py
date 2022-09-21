from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(title="BaseApp", description=("BaseApp"), version="0.0.1")


class Body(BaseModel):
    test: str


@app.get("/", response_class=HTMLResponse)
def hello() -> str:
    return "hello, world!"


@app.get("/aloha", response_class=HTMLResponse)
def aloha(name: str, surname: str) -> str:
    return f"aloha, {name} {surname}"


@app.post("/body", response_class=HTMLResponse)
def with_body(body: Body) -> str:
    return "test " + body.test
