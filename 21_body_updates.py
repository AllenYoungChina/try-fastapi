# Body - Updates
# To update an item you can use the HTTP PUT operation.
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    'foo': {'name': 'Foo', 'price': 50.2},
    'bar': {'name': 'Bar', 'description': 'The bartenders', 'price': 62, 'tax': 20.2},
    'baz': {'name': 'Baz', 'description': None, 'price': 50.2, 'tax': 10.5, 'tags': []},
}


@app.get('/items/{item_id}', response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


# Note: if you don't set an exact value of the property, which has a default value in Pydantic model,
# FastAPI will replace the value you set before with the default value.
@app.put('/items/{item_id}', response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


# Partial updates with PATCH
@app.patch('/items/{item_id}', response_model=Item)
async def update_item_with_patch(item_id: str, item: Item):
    # Retrieve the stored data, and put that data in a Pydantic model.
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    # Generate a dict without default values from the input model (using exclude_unset)
    update_data = item.model_dump(exclude_unset=True)
    # Create a copy of the stored model, updating it\'s attributes with the received
    # partial updates (using the update parameter).
    updated_item = stored_item_model.model_copy(update=update_data)
    # Convert the copied model to something that can be stored in your DB (for example,
    # using the jsonable_encoder).
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
