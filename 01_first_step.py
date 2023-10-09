# The simplest FastAPI file.
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


if __name__ == '__main__':
    # uvicorn first_step:app --reload
    # Note: Even with 'reload=True', the latest change won't take effect after auto reload.
    uvicorn.run('01_first_step:app', reload=True)
