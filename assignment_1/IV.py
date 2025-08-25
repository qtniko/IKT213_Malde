import cv2
import os


def main():
    img_path = os.path.join(os.path.dirname(__file__), 'lena-1.png')
    image = cv2.imread(img_path)

    height, width, channels = image.shape
    size = image.size
    dtype = image.dtype

    print(f"Height: {height}")
    print(f"Width: {width}")
    print(f"Channels: {channels}")
    print(f"Size (number of values in the cubed array): {size}")
    print(f"Data type: {dtype}")


if __name__ == '__main__':
    main()