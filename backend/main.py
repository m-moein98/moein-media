from fastapi import FastAPI
from authentication_app.views import api_router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="")