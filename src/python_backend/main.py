r""" python_backend.main module """


# importing third-party modules ===============================================
from fastapi import (
    FastAPI,
    APIRouter
)


# importing custom modules ====================================================
from .attachment.router import attachment_router


# module variables ============================================================
app: FastAPI = FastAPI(
    title="rate limited api"
)
api_router: APIRouter = APIRouter(
    prefix="/api"
)
version_router: APIRouter = APIRouter(
    prefix="/v1"
)


# 'app' initializations =======================================================
version_router.include_router(
    attachment_router, prefix="/attachment", tags=["attachment"]
)
api_router.include_router(version_router)
app.include_router(api_router)
