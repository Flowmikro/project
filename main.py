from fastapi import FastAPI

from user_api.router import router as user_router

app = FastAPI(name='API')

app.include_router(router=user_router, tags=['User API'])

