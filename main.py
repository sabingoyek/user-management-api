from fastapi import FastAPI
from user.src import router as user_router

app = FastAPI(title="User API", version="0.0.1")

app.include_router(user_router.router)
