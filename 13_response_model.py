# Response Model - Return Type
from typing import Union, Any

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list[str] = []


# Base user model
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


# User model for input
class UserIn(UserBase):
    password: str


# @app.post('/items/')
# async def create_item(item: Item) -> Item:
#     return item
#
#
# @app.get('/items/')
# async def read_items() -> list[Item]:
#     return [
#         Item(name='Portal Gun', price=42.0),
#         Item(name='Plumbs', price=32.0)
#     ]


# There are some cases where you need or want to return some data
# that is not exactly what the type declares, you can use
# the path operation decorator parameter response_model instead of the return type.
@app.post('/items/', response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get('/items/', response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


# @app.post('/users/', response_model=UserBase)
# async def create_user(user: UserIn) -> Any:
#     return user


# To get better editor support with class inheritance and return type.
@app.post('/users/')
async def create_user(user: UserIn) -> UserBase:
    return user


# Return a Response or its subclasses Directly
@app.get('/portal')
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    return JSONResponse(content={'message': 'Here\'s your interdimensional portal.'})


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


# Use the response_model_exclude_unset parameter to only return the value you set.
@app.get('/items/{item_id}', response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


# You can also use the path operation decorator parameters response_model_include and response_model_exclude.
@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]
