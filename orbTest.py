#/usr/bin/env/Python3

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Init orb detector
orb = cv2.ORB_create()

#Processes each frame in the file while init ORB key points
def processFrame(img):
    kp, des = orb.detectAndCompute(img, None)
    points = []

    for p in kp:
        points.append(p)
        print(p)
    
    return img

#Usual boilerplate for displaying video
if __name__ == "__main__":

    #Get your own filepath
    cap = cv2.VideoCapture('/File/path/to/a/video.mp4')

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:
            cv2.imshow('Frame', processFrame(frame))
            key = cv2.waitKey(0)

            if key == ord('q'):
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()