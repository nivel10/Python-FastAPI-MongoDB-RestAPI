import os
from dotenv import load_dotenv
from pymongo import MongoClient
from models.mongo_db import MongoDB, MongoDB_Collections

load_dotenv()

#region old code
# db_settings: MongoDB = {
#     'host': os.getenv('DB_MONGODB_SERVER'),
#     'db': os.getenv('DB_MONGODB_DB'),
#     'collections': {
#         'users': 'users',
#     },
#     'user': os.getenv('DB_MONGODB_USER'),
#     'password': os.getenv('DB_MONGODB_PASSWORD'),
#     'port': int(os.getenv('DB_MONGODB_PORT')),
#     'url': ''
# }
#endregion old code

mongodb_collections: MongoDB_Collections = MongoDB_Collections(
    users='users'
)

mongodb_settings: MongoDB = MongoDB(
    host=os.getenv('DB_MONGODB_SERVER'),
    db=os.getenv('DB_MONGODB_DB'),
    collections= mongodb_collections,
    user=os.getenv('DB_MONGODB_USER'),
    password=os.getenv('DB_MONGODB_PASSWORD'),
    port=int(os.getenv('DB_MONGODB_PORT')),
    url='',
)

#region old code
# db_settings['url'] = f'mongodb://{db_settings['user']}:{db_settings['password']}@{db_settings['host']}:{db_settings['port']}/{db_settings['db']}'
# db_settings['url'] = f'mongodb://{db_settings['user']}:{db_settings['password']}@{db_settings['host']}'
#endregion old code
mongodb_settings.url = f'mongodb://{mongodb_settings.user}:{mongodb_settings.password}@{mongodb_settings.host}'

# # print(db_settings['url'])
# print(db_settings.url)

#region old code
# # conn = MongoClient()[db_settings['db']]
# conn = MongoClient(
#     host=db_settings['url'],
#     port=int(db_settings['port'])
# )[db_settings['db']]
#endregion old code
conn = MongoClient(
    host=mongodb_settings.url,
    port=mongodb_settings.port
)[mongodb_settings.db]