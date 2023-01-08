# Chapter 20 = split video into frames

# step 1: import libraries
import cv2 as cv
import numpy as np

# step 2: function to read the video
cap = cv.VideoCapture('resources/web_output.avi') # read the video


frame_count = 0 # frames counter

# step 3: loop to read the video frame by frame
while True:
    success, frame = cap.read() # read the video frame by frame
    if success == True: # if the video is read successfully
        cv.imwrite(f'resources/frames/frame_' + str(frame_count) + '.jpg', frame) # save the image as a frame
    else:
        break
    frame_count += 1 # increment the frame count by 1 or 2 and so on

# step 4: release the video
cap.release()
