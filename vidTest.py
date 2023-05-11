#/usr/bin/env/Python3

import cv2

cap = cv2.VideoCapture("/Users/schuylerseaborn/desktop/cvtests/assets/testVid.mp4")

if (cap.isOpened() == False):
    print("Error opening the video file")
else:
    fps = cap.get(5)
    print("Frames per second: ", fps, " FPS")

    frameCount = cap.get(7)
    print("Frame count: ", frameCount)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(50)

        if key == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
