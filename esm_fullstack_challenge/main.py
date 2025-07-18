from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from esm_fullstack_challenge import __version__
from esm_fullstack_challenge.dependencies import create_id_sequence_table_if_not_exists
from esm_fullstack_challenge.routers import basic_router, dashboard_router, \
    drivers_router, races_router
from esm_fullstack_challenge.config import CORS_ORIGINS, LOG_LEVEL


logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_id_sequence_table_if_not_exists()
    yield


app = FastAPI(title="F1 DATA API", version=__version__, lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS.split(','),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        'name': app.title,
        'version': app.version,
    }


@app.get("/ping")
def ping():
    return {"ping": "pong"}


app.include_router(basic_router, prefix='', tags=['Basic'])
app.include_router(drivers_router, prefix='/drivers', tags=['Drivers'])
app.include_router(races_router, prefix='/races', tags=['Races'])
app.include_router(dashboard_router, prefix='/dashboard', tags=['Dashboard'])
