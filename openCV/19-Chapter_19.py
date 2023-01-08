# Chapter 19 = Coordinates of an image on the screen and color of a pixel

# step 1: import libraries
import cv2 as cv
import numpy as np

# step 2: define a function to read coordinates of the mouse
def click_event(event, x, y, flags, param): # x and y are the coordinates of the mouse
    if event == cv.EVENT_LBUTTONDOWN: # if left button is pressed
        print(x, ',', y) # print the coordinates of the mouse
        font = cv.FONT_HERSHEY_SIMPLEX # font of the text
        strXY = str(x) + ', ' + str(y) # text to be displayed
        cv.putText(img, strXY, (x, y), font, 0.5, (255, 255, 0), 2) # display the text on the image (img, text, coordinates, font, size, color, thickness)
        cv.imshow('image', img) # display the image
    if event == cv.EVENT_RBUTTONDOWN: # if right button is pressed
        blue = img[y, x, 0] # blue color of the pixel (width, height, color channel)
        green = img[y, x, 1] # green color of the pixel (width, height, color channel)
        red = img[y, x, 2] # red color of the pixel (width, height, color channel)
        font = cv.FONT_HERSHEY_SIMPLEX # font of the text
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red) # text to be displayed (BGR)
        cv.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 2) # display the text on the image (img, text, coordinates, font, size, color, thickness)
        cv.imshow('image', img) # display the image

# step 3: function to read the image
img = cv.imread('resources/lena.png')
cv.imshow('image', img)

# step 4: call the function
cv.setMouseCallback('image', click_event)

# step 5: wait for a key to be pressed
cv.waitKey(0)
cv.destroyAllWindows()


