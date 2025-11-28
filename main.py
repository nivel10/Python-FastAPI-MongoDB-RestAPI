import os
import uvicorn
from fastapi import FastAPI
from routes.user import user_router
from fastapi.middleware.cors import CORSMiddleware

ENV_STATE = os.getenv('ENV_STATE', '')

origins = [
    '*'
]

app = FastAPI(
    title='Python - FastAPI - MongoDB - restAPI',
    description='RestAPI testing',
    version='1.0.0',
    openapi_tags=[
        {'name':'users', 'description': 'user routers',},
        {'name': 'main', 'description': 'main routers'}
    ],
)

app.add_middleware(
     CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(user_router)

@app.get('/', tags=['main'])
async def main():
    return {'section': 'main'}

@app.get('/hello', tags=['main'])
async def hello():
    return {'section': 'main / hello'}

if __name__ == '__main__':
    if ENV_STATE == 'dev':
        uvicorn.run(
            'main:app',
            host='127.0.0.1',
            port=8000,
            reload=True,
            log_level='debug',
        )