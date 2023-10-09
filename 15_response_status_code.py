# Response Status Code
from fastapi import FastAPI, status

app = FastAPI()


# @app.post("/items/", status_code=200)
# async def create_item(name: str):
#     return {"name": name}


# Shortcut to remember the names
@app.post("/items/", status_code=status.HTTP_200_OK)
async def create_item(name: str):
    return {"name": name}
