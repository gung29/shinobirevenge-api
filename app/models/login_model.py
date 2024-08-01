from pydantic import BaseModel

class CheckVersion(BaseModel):
    version: str

class LoginUser(BaseModel):
    username: str
    password: str