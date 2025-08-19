from fastapi import FastAPI
from routes.user import user_router

app = FastAPI(
    title='Python - FastAPI - MongoDB - restAPI',
    description='RestAPI testing',
    version='1.0.0'
)
app.include_router(user_router)

@app.get('/', tags=['main'])
async def hello():
    return {'message': 'hello world'}