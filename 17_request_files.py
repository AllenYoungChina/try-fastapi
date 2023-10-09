# Request Files
from typing import Annotated, Union

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


# Use File for small file, because the whole contents will be stored in memory.
# To declare File bodies, you need to use File, because otherwise
# the parameters would be interpreted as query parameters or body (JSON) parameters.
# @app.post('/files/')
# async def create_file(file: Annotated[bytes, File()]):
#     return {'file_size': len(file)}
#
#
# # Use UploadFile for large file.
# @app.post('/uploadfile/')
# async def create_upload_file(file: UploadFile):
#     if file.content_type == 'text/plain':
#         contents = await file.read()
#         print(contents.decode())
#     return {'filename': file.filename}


# Optional File Upload
# @app.post('/files/')
# async def create_file(file: Annotated[Union[bytes, None], File()] = None):
#     if not file:
#         return {'message': 'No file sent'}
#     else:
#         return {'file_size': len(file)}
#
#
# @app.post('/uploadfile/')
# async def create_upload_file(file: Union[UploadFile, None] = None):
#     if not file:
#         return {'message': 'No upload file sent'}
#     else:
#         return {'filename': file.filename}


# Multiple File Uploads with Additional Metadata
@app.post("/files/")
async def create_files(
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
