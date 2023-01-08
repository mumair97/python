import cv2 as cv
import numpy as np

img = cv.imread("resources/lena.png")  # read image from resources folder

print("The size of our original image is = ", img.shape)


# resize image
imgResize = cv.resize(img, (500, 700))  # resize image (width, height)
print("The size of our image is = ", imgResize.shape)

# crop image
imgCropped = img[0:300, 0:400]  # crop image (height, width)

cv.imshow("Original", img)  # display image
# cv.imshow("Resized", imgResize)  # display image resized
cv.imshow("Cropped", imgCropped)  # display image cropped


cv.waitKey(0)  # wait for any key to exit
cv.destroyAllWindows()  # destroy all windows

