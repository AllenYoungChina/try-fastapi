# Form Data
from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


# To declare form bodies, you need to use Form explicitly, because without it
# the parameters would be interpreted as query parameters or body (JSON) parameters.
@app.post('/login/')
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {'username': username}
