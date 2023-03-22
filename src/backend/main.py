r""" backend.main module """


# importing third-party modules ===============================================
from fastapi import (
    FastAPI,
    APIRouter,
    Query,
    status
)
from fastapi.responses import JSONResponse


# importing custom modules ====================================================
from .service import get


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


PatentUcid = str
UcidQuery = Query(
    ..., 
    regex=r"[A-Z]{2}-[A-Z0-9]{4,}-[A-Z]{1,2}[0-9]{0,1}", 
    example="US-9145048-B2"
)


# path operations =============================================================
@version_router.get(
    path="/attachment/list"
)
def get_attachment_list(ucid: PatentUcid = UcidQuery) -> JSONResponse:
    return JSONResponse(content=get(ucid), status_code=status.HTTP_200_OK)


# 'app' initializations =======================================================
api_router.include_router(version_router)
app.include_router(api_router)
