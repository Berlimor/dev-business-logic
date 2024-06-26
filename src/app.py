from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
import requests

from .operator1 import operator
from .exceptions import LicensePlateError
from .config import settings
from .models import (
    OperatorStopResponse,
    ManualInput,
    ProductionSchema,
    ProductionSchemaStage,
)

app = FastAPI(title="Test business-logic service")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "PATCH", "DELETE", "PUT"],
    allow_headers=["*"],
)


@app.post("/operator/manual-input")
def start_operator_with_manual_input(manual_input: ManualInput) -> Response:
    """
    If the camera failed to get a license plate number, this endpoint accepts
    the manual input of the plate number.
    """
    try:
        operator._set_license_plate(manual_input.license_plate)
        operator.start_recording()

    except Exception as e:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    return Response(status_code=status.HTTP_200_OK)


@app.post("/operator/start")
def start_operator_process(prod_schema: ProductionSchema):
    """Given the id of a camera, start the operator process."""
    try:
        operator.get_back_plate()
        operator.start_recording()

    except LicensePlateError:
        # If manual input feature is enabled, operator will redirect
        # you to frontend endpoint to input the license plate manually.
        if settings.manual_input:
            return JSONResponse(
                status_code=status.HTTP_504_GATEWAY_TIMEOUT,
                content={"license_plate": True},
            )
        else:
            return Response(status_code=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    return Response(status_code=status.HTTP_200_OK)


@app.get("/stop")
async def stop_operator_process() -> OperatorStopResponse:
    """Stop the operator process, set Operator values to default value."""
    try:
        operator.stop_recording()

    except Exception as e:
        return OperatorStopResponse(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

    operator._set_default()
    return OperatorStopResponse(
        status_code=status.HTTP_200_OK,
        detail="Operator stopped successfully.",
    )


@app.get("/test")
def test_request():
    print("________________________________11111")
    request = ProductionSchema(
        schema_name="Single Vehicle",
        schema_id="2d31e86160d74c6cb6ce83bf249bc853",
        schema_stages=[
            ProductionSchemaStage(
                name="Weight the vehicle",
                type="Weighting",
            ).model_dump()
        ],
        erp_metadata={"order_id": "00000", "water_id": "abc123"},
    )

    print("________________________________22222")

    response = requests.post(
        url="http://business_logic:8001/operator/start", json=request.model_dump()
    )
    return response.json()
