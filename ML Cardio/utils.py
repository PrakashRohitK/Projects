import os
from skimage import io
import numpy as np

def load_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img = io.imread(os.path.join(folder_path, filename))
            images.append(img)
    return np.array(images)
