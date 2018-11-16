import numpy as np
import cv2
from PIL import Image, ImageFilter
import random
import matplotlib.pyplot as plt
# orig = cv2.imread('notfried.jpg')
orig = Image.new('notfried.jpg')
# RGB = random.randrange(100, 100, 3)
# HSV = rgb2hsv(RGB)
# HSV(0, 0, 2) = HSV(0, 0, 2) * 1.2
# # HSV(0, 0, 2) = HSV(0, 0, 2) + 3
# # HSV(HSV > 1) = 1
# RGB = hsv2rgb(HSV)
conv = cv2.cvtColor(orig, cv2.COLOR_BGR2HSV)
color = plt.imshow(conv, cmap="binary")
color.save("color.jpg",JPG)
fried = cv2.imread('color.jpg')
# for x in len()
# HSV = (x, y, z)
cv2.imshow('fried.jpg', fried)
