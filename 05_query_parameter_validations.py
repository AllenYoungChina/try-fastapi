# Query Parameters and String Validations
from typing import Union, Annotated

from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()


# @app.get('/items/')
# async def read_items(
#     q: Annotated[
#         Union[str, None], Query(max_length=50, pattern='^prefix')
#     ] = None
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# To make the query parameter required, just omit the default.
# Pydantic, which is what powers all the data validation and serialization in FastAPI,
# has a special behavior when you use Optional or Union[Something, None] without a default value.
# @app.get('/items/')
# async def read_items(q: Annotated[str, Query(max_length=50, pattern='^prefix')]):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Query parameter list / multiple values
# To declare a query parameter with a type of list, like in the example below,
# you need to explicitly use Query, otherwise it would be interpreted as a request body.
# @app.get("/items/")
# async def read_items(q: Annotated[Union[list[str], None], Query()] = None):
#     query_items = {"q": q}
#     return query_items


# Declare more metadata
@app.get("/items/")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            alias='item-query',
            deprecated=True,
        ),
    ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
