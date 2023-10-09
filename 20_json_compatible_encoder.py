# Using the jsonable_encoder
# It receives an object, like a Pydantic model, and returns a JSON compatible version:
from typing import Union
from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


app = FastAPI()


@app.put('/items/{item_id}')
def update_item(item_id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[item_id] = json_compatible_item_data
