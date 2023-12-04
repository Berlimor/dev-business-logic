from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime


class GeneicResponse(BaseModel):
    status_code: int
    detail: str | None = None

class OperatorStopResponse(GeneicResponse):
    """Da"""