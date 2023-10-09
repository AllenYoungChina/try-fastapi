# Body - Multiple Parameters
from typing import Annotated, Union

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


# Multiple body parameters
@app.put('/items/{item_id}')
async def update_item(
        item_id: Annotated[int, Path(title='The ID of the item to get', gt=0, le=1000)],
        q: Union[str, None] = None,
        user: Union[User, None] = None,
        item: Union[Item, None] = None
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    if item:
        results.update({'item': item})
    if user:
        results.update({'user': user})
    return results


# Singular values in body
@app.put('/items/{item_id}')
async def update_item(
        item_id: int,
        item: Item,
        user: User,
        importance: Annotated[int, Body()],
        q: Union[str, None] = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({'q': q})
    return results


# Embed a single body parameter
# In this case FastAPI will expect a body like:
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     }
# }
# instead of:
# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2
# }
@app.put('/items/{item_id}')
async def update_item(
        item_id: int,
        item: Annotated[Item, Body(embed=True)]
):
    results = {"item_id": item_id, "item": item}
    return results
