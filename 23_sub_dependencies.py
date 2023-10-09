# Sub-dependencies
# You can create dependencies that have sub-dependencies.
# They can be as deep as you need them to be.
from typing import Annotated, Union

from fastapi import FastAPI, Depends, Cookie

app = FastAPI()


def query_extractor(q: Union[str, None] = None):
    return q


def query_or_cookie_extractor(
        q: Annotated[str, Depends(query_extractor)],
        last_query: Annotated[Union[str, None], Cookie()] = None,
):
    if not q:
        return last_query
    return q
