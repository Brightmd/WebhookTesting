from fastapi import APIRouter, status

from webhooktesting._version import __version__
from webhooktesting.schemas.response import (
    HealthCheckResponse,
    VersionResponse,
)

router = APIRouter(prefix="/webhooktesting")


@router.get(
    "/healthcheck",
    summary="Validating general health of API",
    tags=["Diagnostics"],
    responses={
        status.HTTP_200_OK: {
            "description": "Successful Response",
            "model": HealthCheckResponse,
        },
    },
)
def read_healthcheck():
    return HealthCheckResponse(status="OK")


@router.get(
    "/version",
    summary="Validating version of running application",
    tags=["Diagnostics"],
    status_code=status.HTTP_200_OK,
    description="Successful Response",
    response_model=VersionResponse,
)
def read_version():
    return VersionResponse(version=__version__)
