# Chapter 15 = Resolutions of webcam

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


while True:
    ret, frame = cap.read()  # read the video capture object

    if ret == True:
        cv.imshow("Camera", frame)  # display image
        if cv.waitKey(1) & 0xFF == ord('q'):  # wait for 'q' key to exit
            break
    else:
        break

cap.release()  # release the video capture object
cv.destroyAllWindows()  # destroy all windows



