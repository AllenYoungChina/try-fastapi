# Query parameters
from typing import Union

from fastapi import FastAPI
import uvicorn

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):  # with defaults
    return fake_items_db[skip: skip + limit]


@app.get('/items/{item_id}')
# async def read_item(item_id: str, q: str | None = None):  # optional parameters Python 3.10+
async def read_item(item_id: str, q: Union[str, None] = None):  # optional parameters Python 3.6+
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}


@app.get('/users/{user_id}')
async def read_item(user_id: str, needy: str):  # required query parameters
    user = {'user_id': user_id, 'needy': needy}
    return user
