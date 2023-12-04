from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    csv_path: str = "Folder path where csv files are (/*.csv)."
    video_path: str = "./vids"
    img_path: str = "./images"

    ipfs_gateway_uri: str = "http://feecc-ipfs-gateway/publish-to-ipfs/upload-file"
    camera_plates_uri: str = "http://feecc-camera-gateway/license-plate?cam_id=1"
    camera_overview_vid_start: str = "http://feecc-camera-gateway/start-record?cam_id=2"
    camera_overview_vid_stop: str = "http://feecc-camera-gateway/stop-record?cam_id=2"

    manual_input: bool = True


settings = Settings()