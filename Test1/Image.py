import numpy as np
import cv2
import matplotlib.pyplot as plt
# Load an color image in grayscale
img1 = cv2.imread('whatsapp_debug.png')
img=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()