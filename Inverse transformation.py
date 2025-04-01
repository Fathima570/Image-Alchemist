import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the input image
image = cv2.imread('data/Apple.png')  # Replace with your input image file path

# Check if the image was loaded properly
if image is None:
    print("Error: Image not found. Please check the file path!")
else:
    # Perform inverse transformation (255 - pixel_value)
    inverted_image = 255 - image

    # Display the results
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Display original image
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    # Display inverse transformed image (pixel inversion)
    axes[1].imshow(cv2.cvtColor(inverted_image, cv2.COLOR_BGR2RGB))
    axes[1].set_title('Inverted Image (255 - pixel_value)')
    axes[1].axis('off')

    # Show the images
    plt.show()
