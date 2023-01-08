# chapter 12 = Setting of camera or video properties

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) # 0 for default camera

# set the width and height, and brightness of the camera
cap.set(3, 640)   # 3 for width
cap.set(4, 480)   # 4 for height
cap.set(10, 100)  # 10 for brightness

while(cap.isOpened()):
    ret, frame = cap.read()
    # grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)

    if ret == True:
        cv.imshow("OriginalCam", frame)
        # cv.imshow("GrayCam", grayframe)
        # cv.imshow("BinaryCam", binary)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
