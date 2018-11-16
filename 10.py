import numpy as np
import cv2
from PIL import Image, ImageFilter
import random
import matplotlib.pyplot as plt

im_gray = cv2.imread("deepfriedvtwo.jpg", cv2.IMREAD_GRAYSCALE)
im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_HSV)
cv2.imwrite("offfried.jpg",im_color)



# 1500 x 1000
