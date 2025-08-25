import cv2
import os

def print_image_information(img):
    height, width, channels = img.shape
    size = img.size
    dtype = img.dtype

    print(f"Height: {height}")
    print(f"Width: {width}")
    print(f"Channels: {channels}")
    print(f"Size (number of values in the cubed array): {size}")
    print(f"Data type: {dtype}")

def save_camera_outputs(cap):
    fpath = os.path.join(os.path.dirname(__file__), 'solutions', 'camera_outputs.txt')

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

def main():
    img_path = os.path.join(os.path.dirname(__file__), 'lena-1.png')
    img = cv2.imread(img_path)

    cap = cv2.VideoCapture(0)

    print_image_information(img)
    save_camera_outputs(cap)

    cap.release()

if __name__ == '__main__':
    main()