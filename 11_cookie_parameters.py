# Cookie Parameters
# You can define Cookie parameters the same way you define Query and Path parameters.
from typing import Annotated, Union

from fastapi import FastAPI, Cookie

app = FastAPI()


# To declare cookies, you need to use Cookie, because otherwise
# the parameters would be interpreted as query parameters.
@app.get('/items/')
async def read_items(ads_id: Annotated[Union[int, None], Cookie()] = None):
    return {'ads_id': ads_id}
