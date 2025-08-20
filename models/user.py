from pydantic import BaseModel
from typing import Optional

#region old code
# class User_Base(BaseModel):
#     name: str
#     email: str

# class User(User_Base, BaseModel):
#     id: Optional[str]
#     # name: str
#     # email: str
#     password: str

# class User_DB(User_Base, BaseModel):
#     _id: object
#     # name: str
#     # email: str
#     password: str

# # class User_Login():
# #     email: str
# #     password:str

# #     def __init__(self, email: str, password: str):
# #         self.email = email
# #         self.password = password
#endregion old code

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

class User_Login(BaseModel):
    email: str | None
    password: str | None

class User_Not_Password(BaseModel):
    id: Optional[str]
    name: str
    email: str

class User_Before_After(BaseModel):
    before: User
    after: User