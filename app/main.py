from fastapi import FastAPI
from app.api.Router import router
import uvicorn
app = FastAPI()

app.include_router(router)



