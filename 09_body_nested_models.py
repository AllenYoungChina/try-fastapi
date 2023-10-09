# Body - Nested Models
# With FastAPI, you can define, validate, document, and use arbitrarily deeply nested models.
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


# Nested Models
class Image(BaseModel):
    url: HttpUrl  # HttpUrl is one of types supported by Pydantic
    name: str


# You can define an attribute to be a subtype. For example, a Python list:
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    # tags: list = []
    # tags: list[str] = []  # make tags be specifically a "list of strings"
    tags: set[str] = set()  # make every tag unique
    # image: Union[Image, None] = None  # Image is a nested model
    images: Union[list[Image], None] = None  # attributes with lists of submodels


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# Bodies of pure lists
@app.post('/images/multiple/')
async def create_multiple_images(images: list[Image]):
    return images


# Bodies of arbitrary dicts
# In this case, you would accept any dict as long as it has int keys with float values:
@app.post('/index-weights/')
async def create_index_weights(weights: dict[int, float]):
    return weights
