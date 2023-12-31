# Path parameters
from enum import Enum

from fastapi import FastAPI
import uvicorn

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lnet = 'lnet'


app = FastAPI()


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}

    if model_name.value == 'lnet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}

    return {'model_name': model_name, 'message': 'Have some residuals'}


@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}
