from typing import Optional
from pydantic import BaseModel
from uuid import UUID,uuid4
from enum import Enum



class Gender(str,Enum):
    male = "male"
    female = "female"

class Role(str,Enum):

    admin = "admin"
    user = "user"
class AdminData(BaseModel):
    AdminId:str
    AdminPassword:str
class person(BaseModel):
    id:str
    firstName : str
    lastName : str
    middleName:Optional[str]= None
    password:str
    gender : Gender
    role : Role

    adminData :AdminData
