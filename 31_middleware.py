# Middleware
# A "middleware" is a function that works with every request before it is processed by any specific path operation.
# And also with every response before returning it.
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)
    return response
