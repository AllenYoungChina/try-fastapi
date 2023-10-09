from fastapi import APIRouter, Depends, HTTPException, status

from ..dependencies import get_token_header

# We know all the path operations in this module have the same path prefix, tags,
# extra responses, dependencies. So, instead of adding all that to each path operation,
# we can add it to the APIRouter.
router = APIRouter(
    prefix='/items',
    tags=['items'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description': 'Not found'}},
)

fake_items_db = {'plumbs': {'name': 'Plumbs'}, 'gun': {'name': 'Portal Gun'}}


@router.get('/')
async def read_items():
    return fake_items_db


@router.get('/{item_id}')
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    return {'name': fake_items_db[item_id]['name'], 'item_id': item_id}


@router.put(
    '/{item_id}',
    tags=['custom'],
    responses={403: {'description': 'Operation forbidden'}}
)
async def update_item(item_id: str):
    if item_id != 'plumbs':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You can only update the item: plumbs'
        )
    return {'item_id': item_id, 'name': 'The great Plumbs'}
