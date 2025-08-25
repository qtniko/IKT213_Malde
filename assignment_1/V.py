import cv2
import os

fpath = os.path.join(os.path.dirname(__file__), 'camera_outputs.txt')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

with open(fpath, "w") as f:
    f.write(f"fps: {fps}\n")
    f.write(f"width: {width}\n")
    f.write(f"height: {height}\n")

cap.release()