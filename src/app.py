from fastapi import FastAPI, Response, status

from .operator1 import operator
from .exceptions import LicensePlateError
from .config import settings
from .models import OperatorStopResponse

app = FastAPI(title="Test business-logic service")

@app.post("/operator/manual-input")
def start_operator_with_manual_input(license_plate: str) -> Response:
    """
    If the camera failed to get a license plate number, this endpoint accepts
    the manual input of the plate number.
    """
    try:
        operator._set_license_plate(license_plate)
        operator.start_recording()
    
    except Exception as e:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    
    return Response(status_code=status.HTTP_200_OK)
    

@app.get("/operator/start")
def start_operator_process(cam_id: int) -> Response:
    """Given the id of a camera, start the operator process."""
    try:
        operator.set_cam_id(cam_id)
        operator.get_back_plate()
        operator.start_recording()

    except LicensePlateError:
        # If manual input feature is enabled, operator will redirect
        # you to frontend endpoint to input the license plate manually.
        if settings.manual_input:
            return OperatorStopResponse(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail="license_plate")
        else:
            return Response(status_code=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    return Response(status_code=status.HTTP_200_OK)

@app.get("/stop", status_code=201)
async def stop_operator_process() -> OperatorStopResponse:
    """Stop the operator process, set Operator values to default value."""
    try:
        operator.stop_recording()

    except Exception as e:
        return OperatorStopResponse(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    operator._set_default()
    return OperatorStopResponse(
        status_code=status.HTTP_201_CREATED, 
        detail="Operator stopped successfully.",
    )