from fastapi import FastAPI,status,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm




secretKey="36ea6ade893c89b327abb784ecf1c40f78d1e27a37a7a4973c1ace197adbc82c"
hashingALG="HS256"
expireTime=30
app = FastAPI()
