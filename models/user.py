from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str

class User_DB(BaseModel):
    _id: object
    name: str
    email: str
    password: str

# class User_Login():
#     email: str
#     password:str

#     def __init__(self, email: str, password: str):
#         self.email = email
#         self.password = password

class User_Login(BaseModel):
    email: str | None
    password: str | None