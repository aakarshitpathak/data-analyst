from ultralytics import YOLO

# pre-trained YOLOv8 Nano model (fast aur lightweight)
model = YOLO("yolov8n.pt")
# Webcam se live object detection (source=0 matlab default camera)
model.predict(
    source = 0, #webcam
    show = True, # Live window will show
    conf = 0.5 #confidence threshold  (50%)
)

