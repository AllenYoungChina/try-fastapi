# Classes as Dependencies
from typing import Annotated, Union

from fastapi import FastAPI, Depends

app = FastAPI()

fake_item_db = [{'item_name': 'Foo'}, {'item_name': 'Bar'}, {'item_name': 'Baz'}]


class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get('/items/')
async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    response = {}
    if commons.q:
        response.update({'q': commons.q})
    items = fake_item_db[commons.skip: commons.skip + commons.limit]
    response.update({'items': items})
    return response


# In the case mentioned above, you can omit the params for Depends.
# async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
#     response = {}
#     if commons.q:
#         response.update({'q': commons.q})
#     items = fake_item_db[commons.skip: commons.skip + commons.limit]
#     response.update({'items': items})
#     return response
