#noise removal

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the color image
img = cv2.imread("./data/noise2.jpeg")  # Updated file name

# Convert to YCrCb color space (Y = brightness, Cr & Cb = color channels)
img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Split channels
y, cr, cb = cv2.split(img_ycrcb)

# Apply Gaussian Blur only on the Y (luminance) channel to remove noise
y_denoised = cv2.GaussianBlur(y, (5, 5), 0)

# Merge back the channels
img_denoised = cv2.merge((y_denoised, cr, cb))

# Convert back to BGR color space
img_denoised = cv2.cvtColor(img_denoised, cv2.COLOR_YCrCb2BGR)

# Display the results
fig, axes = plt.subplots(1, 2, figsize=(20, 5))

axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(cv2.cvtColor(img_denoised, cv2.COLOR_BGR2RGB))
axes[1].set_title('Noise Removed')
axes[1].axis('off')

plt.show()
