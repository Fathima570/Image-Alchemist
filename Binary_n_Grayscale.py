import numpy as np
import cv2
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread("Sunflower.jfif")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,binary_img = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

fig, axes = plt.subplots(1, 3, figsize=(20, 5))

axes[0].imshow(img)
axes[0].set_title('Orginal image')
axes[0].axis('off')

axes[1].imshow(gray,cmap='gray')
axes[1].set_title('Grayscale')
axes[1].axis('off')

axes[2].imshow(binary_img,cmap='gray')
axes[2].set_title('Binary')
axes[2].axis('off')

axes[2].imshow(binary_img,cmap='gray')
axes[2].set_title('Binary')
axes[2].axis('off')
