# Chapter 16 = Saving HD recordings of webcam

import cv2 as cv
import numpy as np

# get the resolution of the webcam
cap = cv.VideoCapture(0)  # create a video capture object

# resolution HD (1280, 720)

def make_1080p(): # Full HD
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p(): # HD
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p(): # VGA or SD
    cap.set(3, 640)
    cap.set(4, 480) # 480p

# make_1080p()
# make_720p()
make_480p()

# how to change the frame rate
cap.set(5, 60)  # 60 fps


# writing format, codec, video writer and file output
# fourcc = cv.VideoWriter_fourcc(*'XVID')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('resources/webcam_output.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height)) 
# 10 is the frame rate, (frame_width, frame_height) is the resolution, isColor=False is for black and white.

# indicates if the video is opened or not
if not cap.isOpened():
    print("Cannot open video")
    exit()

# reading and playing video

while True:
    ret, frame = cap.read()  # takes cap as input and store it in frame
    # grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # takes frame as input and convert it into gray
    # (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)  # takes grayframe as input and convert it into black and white

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    out.write(frame)  # takes frame as input and write it in output.avi
    cv.imshow('frame', frame)  # takes grayframe/binary as input and display it grayframe/binary

    if cv.waitKey(1) == ord('q'):  # press q to exit
        break

cap.release() # release the video capture object
out.release() # release the video writer object
cv.destroyAllWindows() # destroy all windows

