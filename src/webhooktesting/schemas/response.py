from pydantic import BaseModel


class WebhookTesterException(BaseModel):
    error: str


class HealthCheckResponse(BaseModel):
    status: str


class VersionResponse(BaseModel):
    version: str
