from fastapi import FastAPI

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

tags_metadata = [
    {
        'name': 'users',
        'description': 'Operations with users. The **login** logic is also here.',
    },
    {
        'name': 'items',
        'description': 'Manage items. So _fancy_ they have their own docs.',
        'externalDocs': {
            'description': 'Items external docs',
            'url': 'https://fastapi.tiangolo.com/'
        }
    }
]

app = FastAPI(
    # The title of the API.
    title='ChimichangApp',
    # A short description of the API. It can use Markdown.
    description=description,
    # A short summary of the API.
    summary='Deadpool\'s favorite app. Nuff said.',
    # The version of the API.
    version='0.1.1',
    # A URL to the Terms of Service for the API.
    terms_of_service='http://example.com/terms/',
    # The contact information for the exposed API.
    contact={
        'name': 'Deadpoolio the Amazing',
        'url': 'http://x-force.example.com/contact/',
        'email': 'dp@x-force.example.com',
    },
    # The license information for the exposed API.
    license_info={
        'name': '',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
    },
    # Additional metadata for the different tags.
    openapi_tags=tags_metadata,
    # Path to the OpenAPI schema
    # openapi_url=None,
    openapi_url='/api/v1/openapi.json',
    # Docs Urls for Swagger UI
    # docs_url=None,
    docs_url='/documentation',
    # Docs Urls for Swagger UI
    # docs_url=None,
)


@app.get('/users/', tags=['users'])
async def read_users():
    return [{'name': 'Harry'}, {'name': 'Ron'}]


@app.get('/items/', tags=['items'])
async def read_items():
    return [{'name': 'wand'}, {'name': 'flying broom'}]
