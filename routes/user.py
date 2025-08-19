from fastapi import APIRouter, HTTPException, status

user_router = APIRouter(
    prefix='/users',
    tags=['users']
)

@user_router.get('/')
async def get_users():
    try:
        return []
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        )