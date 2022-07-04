import cv2
import numpy as np

def preProcess(path, size1, size2):
    image = cv2.imread(path)
    image = cv2.resize(image, (size1, size2))
    image = np.array(image) 
    image = np.expand_dims(image, axis=0)
    image = np.expand_dims(image, axis=-1)
    return image
