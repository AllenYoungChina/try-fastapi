# Path Operation Configuration
from typing import Union
from enum import Enum

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()


# You can define the (HTTP) status_code to be used in the response of your path operation.
# @app.post('/items/', response_model=Item, status_code=status.HTTP_201_CREATED)
# async def create_item(item: Item):
#     return item


# You can add tags to your path operation, pass the parameter tags with a list of str (commonly just one str):
# And you can store the tags in an Enum for a big application.
class Tags(str, Enum):
    items = 'items'
    users = 'users'


# @app.post('/items/', response_model=Item, tags=[Tags.items])
# async def create_item(item: Item):
#     return item


@app.get('/items/', tags=[Tags.items])
async def read_items():
    return [{'name': 'Foo', 'price': 42}]


@app.get('/users/', tags=[Tags.users])
async def read_users():
    return [{'username': 'johndoe'}]


# You can add a summary and description:
# @app.post(
#     '/items/',
#     response_model=Item,
#     summary='Create an item',
#     description='Create an item with all the information, name, description, price, tax and a set of unique tags',
# )
# async def create_item(item: Item):
#     return item


# Description from docstring
# @app.post('/items/', response_model=Item, summary='Create an item')
# async def create_item(item: Item):
#     """
#     Create an item with all the information:
#
#     - **name**: each item must have a name
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can omit this
#     - **tags**: a set of unique tag strings for this item
#     """
#     return item


# Response description
@app.post(
    '/items/',
    response_model=Item,
    summary='Create an item',
    response_description='The created item'
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


# Deprecate a path operation
@app.get('/elements/', tags=['items'], deprecated=True)
async def read_elements():
    return [{'item_id': 'Foo'}]
