from pydantic import BaseModel


class GeneicResponse(BaseModel):
    status_code: int
    detail: str | None = None

class OperatorStopResponse(GeneicResponse):
    """Da"""