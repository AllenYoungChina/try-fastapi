# Body - Fields
# You can declare validation and metadata inside of Pydantic models using Pydantic's Field.
from typing import Union, Annotated

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title='The description of the item', max_length=300
    )
    price: float
    tax: Union[float, None] = None


# Field works the same way as Query, Path and Body, it has all the same parameters, etc.
@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {'item_id': item_id, 'item': item}
    return results
