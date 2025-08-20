from fastapi import APIRouter, HTTPException, status
from config.db import conn, mongodb_collections
from schemas.user import userEntity, usersEntity, userLoginEntity
from models.user import User, User_DB, User_Login
from bson import ObjectId
from passlib.context import CryptContext
# from passlib.hash import sha256_crypt

crypt = CryptContext(schemes=['bcrypt'])

user_router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@user_router.get('/', response_model=list[User])
async def get_users():
    try:
        rows = conn[mongodb_collections.users].find()
        # print(rows)
        return usersEntity(rows)
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )

@user_router.post('/', response_model=User)
async def create_user(user: User):
    try:
        user_new = dict(user)
        user_new.pop('id')
        user_new['password'] = crypt.hash(user_new['password'])
        # # user_new['password'] = sha256_crypt.encrypt(user_new['password'])
        # user_new['password'] = sha256_crypt.hash(user_new['password'])
        user_new_id = conn[mongodb_collections.users].insert_one(user_new).inserted_id
        user_new_found: User = await find_user(key='_id', value=ObjectId(str(user_new_id)))

        return user_new_found
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )

@user_router.get('/{id}', response_model=User)
async def get_user(id: str):
    try:
        user_found: User = await find_user(key='_id', value=ObjectId(id))
        
        return user_found
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )

@user_router.put('/{id}')
async def update_user(id, user):
    try:
        pass
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )

@user_router.delete('/{id}', response_model=User)
async def delete_user(id: str):
    try:
        user_found: User = await find_user(key='_id', value=ObjectId(id))
        if user_found:
            conn[mongodb_collections.users].find_one_and_delete({'_id': ObjectId(id)})
        
        return user_found
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )

@user_router.post('/login')
async def login_user(user_login: User_Login):
    try:
        if not user_login.email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='email is required'
            )
        elif not user_login.password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='password is required',
            )
        
        user_found: User_DB = conn[mongodb_collections.users].find_one({'email': user_login.email})
        if not user_found:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='email or password incorrect',
            )
        
        password_corect = crypt.verify(user_login.password, user_found['password'])
        if not password_corect:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='email or password incorrect',
            )
        
        return userLoginEntity(user_found)
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )
    
async def find_user(key: str, value: str | ObjectId):
    try:
        user_found: User_DB = conn[mongodb_collections.users].find_one({key: value})

        if not user_found:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'user not fount. {key}: {str(value) if value == object else value}'
            )
        
        return userEntity(user_found)
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )