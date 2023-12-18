from pydantic import BaseModel


class GenericResponse(BaseModel):
    status_code: int
    detail: str | None = None

class OperatorStopResponse(GenericResponse):
    """ """


class OperatorStartResponse(GenericResponse):
    license_plate: bool = False