import math

import cv2
import cvzone
from fastapi import HTTPException
from hyko_sdk.io import Image
from hyko_sdk.models import Ext
from metadata import Inputs, Outputs, Params, StartupParams, func
from ultralytics import YOLO


@func.on_startup
async def load(startup_params: StartupParams):
    global model, device_map
    device_map = startup_params.device_map
    model = YOLO(f"{startup_params.model.name}.pt")
    if device_map == "auto":
        raise HTTPException(
            status_code=500, detail="AUTO not available as device_map in this Tool."
        )


@func.on_execute
async def main(inputs: Inputs, params: Params) -> Outputs:
    image = await inputs.input_image.to_ndarray()
    img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    results = model.predict(
        source=img, conf=params.threshold, iou=params.iou_threshold, device=device_map
    )
    bboxs = results[0].boxes
    names = results[0].names
    for box in bboxs:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        clsi = int(box.cls[0])
        conf = math.ceil(box.conf[0] * 100) / 100
        w, h = int(x2 - x1), int(y2 - y1)
        cvzone.cornerRect(img, (x1, y1, w, h), l=7, rt=1)
        cvzone.putTextRect(
            img,
            f"{names[clsi]} {conf}",
            (max(0, x1), max(20, y1)),
            thickness=1,
            colorR=(0, 0, 255),
            scale=0.9,
            offset=3,
        )
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return Outputs(image=await Image.from_ndarray(img, encoding=Ext.PNG))  # type: ignore
