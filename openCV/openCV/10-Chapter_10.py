# chapter 10 = how to capture a webcamera video and convert it into gray and black and white

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) # 0 for default camera

while(cap.isOpened()):
    ret, frame = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)

    if ret == True:
        cv.imshow("OriginalCam", frame)
        cv.imshow("GrayCam", grayframe)
        cv.imshow("BinaryCam", binary)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()