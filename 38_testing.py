from typing import Annotated, Union

from fastapi import FastAPI, Header, HTTPException, status
from fastapi.testclient import TestClient
from pydantic import BaseModel

fake_secret_token = 'coneofsilence'

fake_db = {
    'foo': {'id': 'foo', 'title': 'Foo', 'description': 'There goes my hero'},
    'bar': {'id': 'bar', 'title': 'Bar', 'description': 'The bartenders'},
}

app = FastAPI()


class Item(BaseModel):
    id: str
    title: str
    description: Union[str, None] = None


@app.get('/items/{item_id}', response_model=Item)
async def read_item(item_id: str, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid X-Token header')
    if item_id not in fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    return fake_db[item_id]


@app.post('/items/', response_model=Item)
async def create_item(item: Item, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid X-Token header')
    if item.id in fake_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Item already exists')
    fake_db[item.id] = item
    return item

client = TestClient(app)


def test_read_item():
    response = client.get('/items/foo', headers={'X-Token': 'coneofsilence'})
    assert response.status_code == 200
    assert response.json() == {
        'id': 'foo',
        'title': 'Foo',
        'description': 'There goes my hero',
    }


def test_read_item_bad_token():
    response = client.get('/items/foo', headers={'X-Token': 'hailhydra'})
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid X-Token header'}


def test_read_inexistent_item():
    response = client.get('/items/baz', headers={'X-Token': 'coneofsilence'})
    assert response.status_code == 404
    assert response.json() == {'detail': 'Item not found'}


def test_create_item():
    response = client.post(
        '/items/',
        headers={'X-Token': 'coneofsilence'},
        json={'id': 'foobar', 'title': 'Foo Bar', 'description': 'The Foo Barters'},
    )
    assert response.status_code == 200
    assert response.json() == {
        'id': 'foobar',
        'title': 'Foo Bar',
        'description': 'The Foo Barters',
    }


def test_create_item_bad_token():
    response = client.post(
        '/items/',
        headers={'X-Token': 'hailhydra'},
        json={'id': 'bazz', 'title': 'Bazz', 'description': 'Drop the bazz'},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid X-Token header'}


def test_create_existing_item():
    response = client.post(
        '/items/',
        headers={'X-Token': 'coneofsilence'},
        json={'id': 'foo', 'title': 'The Foo ID Stealers', 'description': 'There goes my stealer'},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Item already exists'}
