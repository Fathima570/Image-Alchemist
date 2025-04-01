#size and shape of image

import numpy as np
import cv2
img = cv2.imread("data/car.jpg")
height,width=img.shape[:2]
size=img.size
print(f"Image Shape: {height}x{width} pixels")
print(f"Total Pixels (Size): {size}")

