from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
import uvicorn


from config import settings


app = FastAPI(
    title = 'Start App',
    version = '0.0.1'
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key = settings.SESSION_SECRET)



if __name__ == "__main__":
    uvicorn.run('main:app', reload = True)