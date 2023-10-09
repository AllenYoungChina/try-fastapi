# Extra Models
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return 'supersecret' + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print('User saved! ..not really')
    return user_in_db


@app.post('/users/', response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


# You can declare a response to be the Union of two types, that means,
# that the response would be any of the two.
@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]


class OtherItem(BaseModel):
    name: str
    description: str


other_items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


# you can declare responses of lists of objects.
@app.get("/other-items/", response_model=list[OtherItem])
async def read_other_items():
    return other_items


# You can also declare a response using a plain arbitrary dict,
# declaring just the type of the keys and values, without using a Pydantic model.
@app.get('/keyword-weights/', response_model=dict[str, float])
async def read_keyword_weights():
    return {'foo': 2.3, 'bar': 3.4}
