import cv2
img=cv2.imread("Sunflower.jfif")
newImg=cv2.resize(img,(0,0),fy=0.2,fx=0.3)

fig, axes = plt.subplots(1, 2, figsize=(20, 5))

axes[0].imshow(img)
axes[0].set_title('Orginal image')
axes[0].axis('on')

axes[1].imshow(newImg)
axes[1].set_title('Scaled image')
axes[1].axis('on')

