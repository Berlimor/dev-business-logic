from pydantic import BaseModel, Field
from uuid import uuid4


class GenericResponse(BaseModel):
    detail: str | None = None


class OperatorStopResponse(GenericResponse):
    """"""
    ipfs_cid: str="123123132"
    ipfs_link: str="321321321"
    factory_card_id: str="987987987"
    
class OperatorStartResponse(GenericResponse):
    license_plate: bool = False


class ProductionSchemaStage(BaseModel):
    name: str
    type: str | None = None  # noqa: A003
    description: str | None = None
    equipment: list[str] | None = None
    workplace: str | None = None
    duration_seconds: int | None = None


class ProductionSchema(BaseModel):
    schema_id: str = Field(default_factory=lambda: uuid4().hex)
    schema_name: str
    schema_print_name: str | None = None
    schema_stages: list[ProductionSchemaStage]
    components_schema_ids: list[str] | None = None
    parent_schema_id: str | None = None
    schema_type: str | None = None
    erp_metadata: dict[str, str] | None = None
    allowed_positions: list[str] | None = None


class ManualInput(BaseModel):
    license_plate: str | None = None
    weight: str | None = None
