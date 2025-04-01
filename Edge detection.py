import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread('data/flower.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel operator in X direction
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)  # Detects vertical edges

# Apply Sobel operator in Y direction
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)  # Detects horizontal edges

# Combine Sobel X and Y using absolute values
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Normalize to range 0-255 for better visualization
sobel_combined = np.uint8(255 * sobel_combined / np.max(sobel_combined))

# Display results
plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.axis('off')

plt.subplot(1, 4, 2), plt.imshow(sobel_x, cmap='gray')
plt.title('Sobel X'), plt.axis('off')

plt.subplot(1, 4, 3), plt.imshow(sobel_y, cmap='gray')
plt.title('Sobel Y'), plt.axis('off')

plt.subplot(1, 4, 4), plt.imshow(sobel_combined, cmap='gray')
plt.title('Sobel Combined'), plt.axis('off')

plt.show()
