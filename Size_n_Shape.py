import numpy as np
import cv2
img = cv2.imread("Sunflower.jfif")
height,width=img.shape[:2]
size=img.size
print(f"Image Shape: {height}x{width} pixels")
print(f"Total Pixels (Size): {size}")
