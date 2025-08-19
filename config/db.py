import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

db_settings = {
    'host': os.getenv('DB_MONGODB_SERVER'),
    'db': os.getenv('DB_MONGODB_DB'),
    'collections': {
        'users': 'users',
    },
    'user': os.getenv('DB_MONGODB_USER'),
    'password': os.getenv('DB_MONGODB_PASSWORD'),
    'port': os.getenv('DB_MONGODB_PORT'),
    'url': ''
}

# db_settings['url'] = f'mongodb://{db_settings['user']}:{db_settings['password']}@{db_settings['host']}:{db_settings['port']}/{db_settings['db']}'
db_settings['url'] = f'mongodb://{db_settings['user']}:{db_settings['password']}@{db_settings['host']}'
print(db_settings['url'])

# conn = MongoClient()[db_settings['db']]
conn = MongoClient(
    host=db_settings['url'],
    port=int(db_settings['port'])
)[db_settings['db']]