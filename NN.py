import cv2
from skimage import data

img = data.chelsea()


cv2.imshow('Chelsea', img)

cv2.waitKey(0)