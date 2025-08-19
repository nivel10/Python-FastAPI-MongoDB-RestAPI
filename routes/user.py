from fastapi import APIRouter, HTTPException, status
from config.db import conn, mongodb_settings, mongodb_collections
from schemas.user import userEntity, usersEntity
from models.user import User
from bson import ObjectId

user_router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@user_router.get('/')
async def get_users():
    try:
        rows = conn[mongodb_collections.users].find()
        print(rows)
        return usersEntity(rows)
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )

@user_router.post('/')
async def create_user(user: User):
    try:
        user_new = dict(user)
        user_new.pop('id')
        user_new_id = conn[mongodb_collections.users].insert_one(user_new).inserted_id
        user_new_find = await get_user(id=str(user_new_id))

        return user_new_find
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )

@user_router.get('/{id}')
async def get_user(id: str):
    try:
        user_find = conn[mongodb_collections.users].find_one({'_id': ObjectId(id)})
        if not user_find:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'user not found. Id: {id}'
            )
        
        return userEntity(user_find)
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )

@user_router.put('/{id}')
async def create_user(id, user):
    try:
        pass
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )

@user_router.delete('/{id}')
async def create_user():
    try:
        pass
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )