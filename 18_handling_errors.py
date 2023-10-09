# Handling Errors
from fastapi import FastAPI, status, Request
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()

items = {'foo': 'The Foo Wrestlers'}


# When raising an HTTPException, you can pass any value that can be converted to JSON
# as the parameter detail, not only str. They are handled automatically by FastAPI and converted to JSON.
# @app.get('/items/{item_id}')
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
#     return {'item': items[item_id]}


# Add custom headers
# @app.get('/items/{item_id}')
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail='Item not found',
#             headers={'X-Error': 'There goes my error'},
#         )
#     return {'item': items[item_id]}


# Install custom exception handlers
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        content={'message': f'Opps! {exc.name} did something. There goes a rainbow...'}
    )


@app.get('/unicorns/{name}')
async def read_unicorn(name: str):
    if name == 'yolo':
        raise UnicornException(name=name)
    return {'unicorn_name': name}


# Override the default exception handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)
