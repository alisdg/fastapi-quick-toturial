from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.pages.dashboard import general_pages_router
from database.session import engine
from database.base import Base
from core.config import settings
from apis.base import api_router


def include_router(app):
    app.include_router(api_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    configure_static(app)
    include_router(app)
    create_tables()
    return app


app = start_application()

# app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
#
#
# @app.get("/gg/{name}")
# async def say_gg(name: str):
#     return {"message": f"gg {name}"}
