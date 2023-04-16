r""" python_backend.attachment.router module """


# importing third-party modules ===============================================
from fastapi import (
    APIRouter,
    Query,
    status
)
from fastapi.responses import JSONResponse


# importing custom modules ====================================================
from .service import get_list


# module variables ============================================================
PatentUcid = str
UcidUrlQueryParameter = Query(
    ..., 
    regex=r"[A-Z]{2}-[A-Z0-9]{4,}-[A-Z]{1,2}[0-9]{0,1}", 
    example="US-9145048-B2"
)
attachment_router: APIRouter = APIRouter()


# path operations =============================================================
@attachment_router.get(
    path="/list"
)
def get_attachment_list(
    ucid: PatentUcid = UcidUrlQueryParameter
    ) -> JSONResponse:
    return JSONResponse(content=get_list(ucid), status_code=status.HTTP_200_OK)
