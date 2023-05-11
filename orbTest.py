#/usr/bin/env/Python3

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Init orb detector
orb = cv2.ORB_create()

#Processes each frame in the file while init ORB key points
def processFrame(img):
    kp, des = orb.detectAndCompute(img, None)

    #Test for kp's to see if we're getting any
    points = []

    for p in kp:
        u, v = map(lambda x: int(round(x)), p.pt)
        cv2.circle(img, (u, v), color=(0, 255, 0), radius=4)
        points.append(p)
        print(p)
    
    return img

#Usual boilerplate for displaying video
if __name__ == "__main__":

    #Get your own filepath
    cap = cv2.VideoCapture('/Users/schuylerseaborn/desktop/assets/001.mp4')

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