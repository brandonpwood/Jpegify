import numpy as np
import cv2

img_name = './628x471.jpg'

# Load the image twice and add
img = cv2.imread(img_name)
img2 = cv2.imread(img_name)
res = cv2.add(img, img2)

# Initialize window and display res
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',res)

# Quit with escape key
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
