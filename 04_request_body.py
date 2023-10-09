# Request body
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Python 3.10+
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict


# Request body + path parameters
# @app.put('/items/{item_id}')
# async def create_item(item_id: int, item: Item):
#     return {'item_id': item_id, **item.model_dump()}


# Request body + path + query parameters
@app.put('/items/{item_id}')
async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
    results = {'item_id': item_id, **item.model_dump()}
    if q:
        results.update({'q': q})
    return results
