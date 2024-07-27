from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from other.admin import admin
from starlette.middleware.sessions import SessionMiddleware
import uvicorn

from other import exceptions
from config import settings


app = FastAPI(
    title = 'Start App',
    version = '0.0.1',
)

admin.mount_to(app)


# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key = settings.SESSION_SECRET)



# Exceptions
app.add_exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR, exceptions.exception_500)


# Routing
from app.auth.router import router as auth_router

app.include_router(auth_router)



if __name__ == "__main__":
    uvicorn.run('main:app', reload = True)