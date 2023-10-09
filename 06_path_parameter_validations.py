# Path Parameters and Numeric Validations
from typing import Union, Annotated

from fastapi import FastAPI, Path, Query
import uvicorn

app = FastAPI()


# A path parameter is always required as it has to be part of the path.
# @app.get('/items/{item_id}')
# async def read_item(item_id: Annotated[int, Path(title='The ID of the item to get')],
#                     q: Annotated[Union[str, None], Query()] = None):
#     result = {'item_id': item_id}
#     if q:
#         result.update({'q': q})
#     return result


# Number validations: greater than and less than or equal
@app.get('/items/{item_id}')
async def read_item(
    item_id: Annotated[int, Path(title='The ID of the item to get', gt=10, le=1000)],
    q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results
