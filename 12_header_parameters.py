# Header Parameters
# You can define Header parameters the same way you define Query, Path and Cookie parameters.
from typing import Union, Annotated

from fastapi import FastAPI, Header

app = FastAPI()


# To declare headers, you need to use Header, because otherwise
# the parameters would be interpreted as query parameters.
# By default, Header will convert the parameter names characters
# from underscore (_) to hyphen (-) to extract and document the headers,
# so, you can use user_agent as you normally would in Python code,
# instead of needing to capitalize the first letters as User_Agent or something similar.
@app.get('/items/')
async def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
    return {'User-Agent': user_agent}


# Duplicate headers
# It is possible to receive duplicate headers. That means, the same header with multiple values.
# @app.get('/items/')
# async def read_items(x_token: Annotated[Union[list[str], None], Header()] = None):
#     return {'X-Token': x_token}
