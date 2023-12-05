from pydantic import BaseModel


class GenericResponse(BaseModel):
    status_code: int
    detail: str | None = None

class OperatorStopResponse(GenericResponse):
    """Da"""

class OperatorStartResponse(GenericResponse):
    """Da"""
