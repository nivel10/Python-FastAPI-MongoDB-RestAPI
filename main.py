from fastapi import FastAPI
from routes.user import user_router

app = FastAPI(
    title='Python - FastAPI - MongoDB - restAPI',
    description='RestAPI testing',
    version='1.0.0',
    openapi_tags=[
        {'name':'users', 'description': 'user routers',},
        {'name': 'main', 'description': 'main routers'}
    ],
)
app.include_router(user_router)

@app.get('/', tags=['main'])
async def main():
    return {'section': 'main'}

@app.get('/hello', tags=['main'])
async def hello():
    return {'section': 'main / hello'}