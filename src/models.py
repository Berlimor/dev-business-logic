from pydantic import BaseModel, Field
from uuid import uuid4


class GenericResponse(BaseModel):
    status_code: int
    detail: str | None = None


class OperatorStopResponse(GenericResponse):
    """ """


class OperatorStartResponse(GenericResponse):
    license_plate: bool = False


class ProductionSchemaStage(BaseModel):
    name: str
    stage_id: str
    type: str | None = None  # noqa: A003
    description: str | None = None
    equipment: list[str] | None = None
    workplace: str | None = None
    duration_seconds: int | None = None


class ProductionSchema(BaseModel):
    schema_id: str = Field(default_factory=lambda: uuid4().hex)
    unit_name: str
    unit_short_name: str | None = None
    production_stages: list[ProductionSchemaStage] | None = None
    required_components_schema_ids: list[str] | None = None
    parent_schema_id: str | None = None
    schema_type: str | None = None
    erp_metadata: dict[str, str] | None = None


class ManualInput(BaseModel):
    license_plate: str | None = None
    weight: str | None = None
