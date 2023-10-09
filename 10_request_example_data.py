# Declare Request Example Data
from typing import Annotated, Union

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "name": "foo",
    #                 "description": "A very nice Item",
    #                 "price": 35.4,
    #                 "tax": 3.2
    #             }
    #         ]
    #     }
    # }


# @app.put('/items/{item_id}')
# async def update_item(item_id: int, item: Item):
#     results = {'item_id': item_id, 'item': item}
#     return results


# Body with multiple examples
@app.put('/items/{item_id}')
async def update_item(
        item_id: int,
        item: Annotated[
            Item,
            Body(
                examples=[
                    {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                    {
                        "name": "Bar",
                        "price": "35.4",
                    },
                    {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                ]
            )
        ]
):
    results = {"item_id": item_id, "item": item}
    return results
