# Get Current User
from typing import Annotated, Union

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr

app = FastAPI()

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


class User(BaseModel):
    username: str
    email: Union[EmailStr, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


def fake_decode_token(token):
    return User(
        username=token + 'fakedecoded', email='john@example.com', full_name='John Doe'
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_schema)]):
    user = fake_decode_token(token)
    return user


@app.get('/users/me')
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
