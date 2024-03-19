import asyncio
from time import monotonic
from pydantic import BaseModel
from fastapi import FastAPI

SLEEP_DURATION_SEC = 3

app = FastAPI()
lock = asyncio.Lock()


async def work() -> None:
    await asyncio.sleep(SLEEP_DURATION_SEC)


class TestResponse(BaseModel):
    elapsed: float


@app.get("/test", response_model=TestResponse)
async def test() -> TestResponse:
    ts1 = monotonic()
    async with lock:
        await work()
    ts2 = monotonic()
    return TestResponse(elapsed=ts2 - ts1)
