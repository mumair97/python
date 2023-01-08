# chapter 11 = Saving Webcamera Video and Writing

import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)  # takes webcamera as input and store it in cap

# writing format, codec, video writer and file output
# fourcc = cv.VideoWriter_fourcc(*'XVID')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('resources/web_output.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height), isColor=False)

# indicates if the video is opened or not
if not cap.isOpened():
    print("Cannot open video")
    exit()

# reading and playing video

while True:
    ret, frame = cap.read()  # takes cap as input and store it in frame
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # takes frame as input and convert it into gray
    # (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)  # takes grayframe as input and convert it into black and white

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    out.write(grayframe)  # takes frame as input and write it in output.avi
    cv.imshow('frame', grayframe)  # takes grayframe/binary as input and display it grayframe/binary

    if cv.waitKey(1) == ord('q'):  # press q to exit
        break

cap.release()
out.release()
cv.destroyAllWindows()

