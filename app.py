import os
import tempfile
import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import cv2
from ultralytics import YOLO

model = YOLO('weights/best.onnx')

app = FastAPI(title = 'Vehicle Detection')

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

video_path_global = None
object_state = {}
count_id = set()
up = 0
down = 0

def process(frame):
    global object_state, count_id, up, down
    result = model.track(frame, tracker = 'bytetrack.yaml', persist = True, conf = 0.3, imgsz = 512)
    ann = result[0].plot()
    height = ann.shape[0]
    middle = height // 2

    cv2.line(ann, (0, middle), (ann.shape[1], middle), (255, 255, 0), 2)

    if result[0].boxes is not None:
        for box in result[0].boxes:
            if box.id is None:
                continue
            track_id = int(box.id)
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)
            cv2.circle(ann, (center_x, center_y), 4, (0, 0, 255), -1)
            if track_id not in object_state:
                object_state[track_id] = center_y
                continue
            prev_y = object_state[track_id]
            if prev_y < middle and center_y >= middle:
                if track_id not in count_id:
                    down += 1
                    count_id.add(track_id)
            elif prev_y > middle and center_y <= middle:
                if track_id not in count_id:
                    up += 1
                    count_id.add(track_id)
            object_state[track_id] = center_y
    cv2.putText(ann, f"UP: {up}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(ann, f"DOWN: {down}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return ann

def video():
    global video_path_global
    cap = cv2.VideoCapture(video_path_global)
    if not cap.isOpened():
        print("Error: Cannot open video")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        result = process(frame)
        _, buffer = cv2.imencode('.jpg', result)
        frame_bytes = buffer.tobytes()
        yield(b"--frame\r\n"
              b'Content-Type: image/jpeg\r\n\r\n' 
              + frame_bytes + 
              b'\r\n'
              )
    cap.release()

@app.get("/")
def home():
    return FileResponse("templates/index.html")

@app.post("/upload")
async def predict_video(file: UploadFile = File(...)):
    global video_path_global, object_state, count_id, up, down

    object_state = {}
    count_id = set()
    up = 0
    down = 0

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp:
        temp.write(await file.read())
        video_path_global = temp.name

    return {'message': 'Video Uploaded Successfully.'}

@app.get('/stream')
def stream():
    if video_path_global is None:
        return {'error': 'No Video Uploaded.'}
    return StreamingResponse(
        video(),
        media_type= 'multipart/x-mixed-replace; boundary=frame'
    )
