import operator
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

OPERATIONS = {
    "add": operator.add,
    "sub": operator.sub,
    "mul": operator.mul,
    "div": operator.truediv,
}

app = FastAPI()


class CalcRequest(BaseModel):
    a: float
    b: float
    op: Literal["add", "sub", "mul", "div"]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/calc")
def calc(payload: CalcRequest) -> dict[str, float]:
    return {"result": OPERATIONS[payload.op](payload.a, payload.b)}
