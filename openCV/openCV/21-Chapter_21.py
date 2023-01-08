# Chapter 21 = how to detect specific color in an image

# step 1: import libraries
import cv2 as cv
import cv2 as imshow
import numpy as np

# read image
img = cv.imread('resources/lena.png')

# convert to hsv (hue, saturation, value)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV) # create hsv image

# # slider for hsv
# hue = 0-179
# saturation = 0-255
# value = 0-255
# lower = np.array([h_min, s_min, v_min]) # lower bound
# upper = np.array([h_max, s_max, v_max]) 

# # sliders
# def slider(x): 
#     pass

# cv.namedWindow('Tracking')
# cv.createTrackbar('LH', 'Tracking', 0, 179, slider) # lower hue
# cv.createTrackbar('LS', 'Tracking', 0, 255, slider) # lower saturation
# cv.createTrackbar('LV', 'Tracking', 0, 255, slider) # lower value
# cv.createTrackbar('UH', 'Tracking', 179, 179, slider) # upper hue
# cv.createTrackbar('US', 'Tracking', 255, 255, slider) # upper saturation
# cv.createTrackbar('UV', 'Tracking', 255, 255, slider) # upper value






# # define range of blue color in hsv
# lower_blue = np.array([110, 50, 50]) # lower bound of blue
# upper_blue = np.array([130, 255, 255]) # upper bound of blue

# # threshold the hsv image to get only blue colors
# mask = cv.inRange(hsv_img, lower_blue, upper_blue) # mask = image with only blue

# # bitwise and mask and original image
# res = cv.bitwise_and(img, img, mask=mask) # res = image with only blue

# show images
cv.imshow('image', img)
# cv.imshow('mask', mask)
# cv.imshow('res', res)
cv.imshow('hsv', hsv_img)

cv.waitKey(0)
cv.destroyAllWindows()
