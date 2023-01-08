# Chapter 13 = basic fucntions or manipulations in opencv
# see the test_openCV.py file for more details

import cv2 as cv
import numpy as np

img = cv.imread("resources/lena.png")  # read image from resources folder
# print("The size of our original image is = ", img.shape)



# resize image
imgResize = cv.resize(img, (300, 200))  # resize image (width, height)

# gray image
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # convert image into gray (BGR2GRAY)

# blur image
imgBlur = cv.GaussianBlur(img, (7, 7), 0)  # convert image into blur (odd number, odd number, sigmaX)

# edge detection
imgCanny = cv.Canny(img, 100, 100)  # convert image into edge detection (image, threshold1, threshold2)

# dilation (increase the thickness of the edge)
kernel = np.ones((3, 3), np.uint8) # create a kernel (matrix) of 5x5
imgDilation = cv.dilate(imgCanny, kernel, iterations=1)  # convert image into dilation (image, kernel, iterations)

# erosion (decrease the thickness of the edge)
imgEroded = cv.erode(imgDilation, kernel, iterations=1)  # convert image into erosion (image, kernel, iterations)

# crop image
print("The size of our original image is: ", img.shape)  # print the shape of the image
imgCrop = img[0:200, 100:500]  # crop image (height, width)



# display image

cv.imshow("Original", img)  # display image
# cv.imshow("Resized", imgResize)  # display image
# cv.imshow("Gray", imgGray)  # display image
# cv.imshow("Blur", imgBlur)  # display image
# cv.imshow("Canny", imgCanny)  # display image
# cv.imshow("Dilation", imgDilation)  # display image
# cv.imshow("Eroded", imgEroded)  # display image
cv.imshow("Crop", imgCrop)  # display image

cv.waitKey(0)  # wait for any key to exit
cv.destroyAllWindows()  # destroy all windows
