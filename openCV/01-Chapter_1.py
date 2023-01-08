# library import
# pip install opencv-python
import cv2 as cv

img = cv.imread("resources/image.jpg")

cv.imshow("Pehli Image", img)
cv.waitKey(0)
