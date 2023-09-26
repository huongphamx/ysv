from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ysv.router_v1 import router as router_v1

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_v1, prefix="/api/v1")
