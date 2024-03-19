import asyncio
import pytest
from httpx import AsyncClient
from main import app, SLEEP_DURATION_SEC

N_CLIENTS = 3
N_REQUESTS_PER_CLIENT = 3
BASE_URL = "http://0.0.0.0:8000"


@pytest.mark.asyncio
async def test_work() -> None:
    clients = [AsyncClient(app=app) for _ in range(N_CLIENTS)]
    tasks = []
    for cl in clients:
        for _ in range(N_REQUESTS_PER_CLIENT):
            tasks.append(cl.get(BASE_URL + "/test"))

    responses = await asyncio.gather(*tasks)
    elapsed = [r.json()['elapsed'] for r in responses]
    diffs = [second - first for first, second in zip(elapsed[:-1], elapsed[1:])]

    assert all([d >= SLEEP_DURATION_SEC for d in diffs])
