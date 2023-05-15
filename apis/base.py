from fastapi import APIRouter

from apis.v1 import pages
from apis.v1 import users

api_router = APIRouter()
api_router.include_router(pages.general_pages_router, prefix="", tags=["general_pages"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
