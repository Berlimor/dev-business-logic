from loguru import logger

from .exceptions import LicensePlateError


class _Operator:
    def __init__(self) -> None:
        self.license_plate: str | None = None
        self.manual_input: bool = False # If the license plate was inputted manually


    def get_back_plate(self) -> None:
        """Get the back license plate number through feecc-camera-gateway"""
        raise LicensePlateError("Could not get license plate number")

    def _set_license_plate(self, license_plate: str):
        self.license_plate = license_plate
        self.manual_input = True

    def start_recording(self) -> None:
        """Start recording a video through feecc-camera-gateway"""
        logger.info("Camera started recording.")

    def stop_recording(self) -> None:
        """Stop recording a video through feecc-camera-gateway and get it's path"""
        logger.info("Camera stopped recording")

    def _set_default(self):
        self.license_plate = None
        self.cam_id = None
        self.manual_input = False

operator = _Operator()