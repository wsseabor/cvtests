#/usr/bin/env/Python3

import cv2


#Read image in grayscale, 0 flag 
img = cv2.imread('/File/path/to/a/pic.jpg', 0)

#Read image in color, BGR, 1 flag
colorImg = cv2.imread('/File/path/to/a/pic.jpg', 1)

#Display an image in a window, grayscale
cv2.imshow('grayscale image', img)

#Display an image in a window, color
cv2.imshow('color image', colorImg)

#Key press that closes the image window
cv2.waitKey(0)

#Destroys created windows
cv2.destroyAllWindows()