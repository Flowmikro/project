from fastapi import FastAPI

from user_api.router import router as user_router
from user_data.router import router as user_data_router

app = FastAPI(name='API')

app.include_router(router=user_router, tags=['User'])
app.include_router(router=user_data_router, tags=['User Data'])

