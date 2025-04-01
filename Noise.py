import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the color image
img = cv2.imread("Noisy_img.jfif")

# Chech if image is loaded
if img is None:
    print("Error: Image not found.Check the file path...")
else:
    #Apply bilateral filter for noise removal while preserving edges
    img_denoised = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # Display the results
    fig, axes = plt.subplots(1, 2, figsize=(20, 5))

    axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    axes[1].imshow(cv2.cvtColor(img_denoised, cv2.COLOR_BGR2RGB))
    axes[1].set_title('Denoised image')
    axes[1].axis('off')

    plt.show()
