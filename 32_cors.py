# CORS (Cross-Origin Resource Sharing)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# It's also possible to declare the list as "*" (a "wildcard") to say that all are allowed.
# But that will only allow certain types of communication, excluding everything that involves
# credentials: Cookies, Authorization headers like those used with Bearer Tokens, etc.
# So, for everything to work correctly, it's better to specify explicitly the allowed origins.
origins = [
    'http://localhost.tiangolo.com',
    'https://localhost.tiangolo.com',
    'http://localhost',
    'http://localhost:8080',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
async def main():
    return {'message': 'Hello World'}
