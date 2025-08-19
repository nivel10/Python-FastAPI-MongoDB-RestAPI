class MongoDB_Collections():
    users: str

    def __init__(self, users: str):
        self.users = users

class MongoDB():
    host: str
    db:str
    collections: MongoDB_Collections
    user: str
    password: str
    port: int
    url: str

    def __init__(
            self, 
            host:str, 
            db: str, 
            collections: MongoDB_Collections, 
            user: str, 
            password: str, 
            port: int,
            url: str,
    ):
        self.host = host
        self.db = db
        self.collections = collections
        self.user = user
        self.password = password
        self.port = port
        self.url = url
