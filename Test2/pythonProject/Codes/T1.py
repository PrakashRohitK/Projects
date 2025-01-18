import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread("C:\\Users\\kpbrb\\Downloads\\IMG1.jpg")

# Convert the image to grayscale
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold to create a binary image
# Adjust the threshold values to be in a typical grayscale range
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 128, 255, cv2.THRESH_BINARY)

# Display the images using matplotlib
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Display original image
axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
axs[0].axis('off')

# Display grayscale image
axs[1].imshow(grayImage, cmap='gray')
axs[1].set_title('Gray Image')
axs[1].axis('off')

# Display black and white (binary) image
axs[2].imshow(blackAndWhiteImage, cmap='gray')
axs[2].set_title('Black and White Image')
axs[2].axis('off')

# Show the plot
plt.show()
