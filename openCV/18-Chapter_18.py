# Chapter 18 = how to change the perspective of an image

# step 1: import libraries
import cv2 as cv
import numpy as np

# step 2: define a function to change the perspective of an image
def change_perspective(event, x, y, flags, param): # x and y are the coordinates of the mouse
    if event == cv.EVENT_LBUTTONDOWN: # if left button is pressed
        print(x, ',', y) # print the coordinates of the mouse
        points.append((x, y)) # add the coordinates to the list
        if len(points) >= 4: # if there are 4 points
            width, height = 550, 450 # width and height of the image
            pts1 = np.float32(points) # convert the list to a numpy array
            pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]]) # coordinates of the new image
            matrix = cv.getPerspectiveTransform(pts1, pts2) # matrix to change the perspective
            imgOutput = cv.warpPerspective(img, matrix, (width, height)) # change the perspective of the image
            cv.imshow('Output', imgOutput) # display the image

# step 3: function to read the image
img = cv.imread('resources/cards.png')
cv.imshow('image', img)

# step 4: call the function
points = [] # list to store the coordinates of the mouse
cv.setMouseCallback('image', change_perspective)

# step 5: wait for a key to be pressed
cv.waitKey(0)
cv.destroyAllWindows()

