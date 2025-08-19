from fastapi import APIRouter, HTTPException, status
from config.db import conn, db_settings
from schemas.user import userEntity, usersEntity

user_router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@user_router.get('/')
async def get_users():
    try:
        rows = conn[db_settings['collections']['users']].find()
        #print(rows)
        return usersEntity(rows)
        pass
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )

@user_router.post('/')
async def create_user(user):
    try:
        pass
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )

@user_router.post('/{id}')
async def get_user(id):
    try:
        pass
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