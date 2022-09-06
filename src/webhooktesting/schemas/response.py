from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    status: str


class VersionResponse(BaseModel):
    version: str
