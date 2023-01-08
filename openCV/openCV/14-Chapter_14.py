# Chapter 14 = Shapes and Texts

import cv2 as cv
import numpy as np

# draw a canvas (zeros for black and ones for white)
img = np.zeros((600, 600))  # create a black image (height, width)
img1 = np.ones((600, 600))  # create a white image (height, width)
# print(img.shape)  # print the shape of the image

# add color to the canvas
colored_img = np.zeros((600, 600, 3), np.uint8)  # create a black image (height, width, color)
colored_img[:] = 0, 255, 0  # add color to the image (BGR)

colored_img[100:300, 100:500] = 0, 0, 255  # add color to a specific area of the image (BGR)

# colored_img1 = np.ones((512, 512, 3), np.uint8)  # create a white image (height, width, color)


# draw a line
cv.line(colored_img, (0, 0), (600, 600), (255, 0, 0), 30)  # draw a line (image, start point, end point, color, thickness)
cv.line(colored_img, (0,0), (colored_img.shape[0], colored_img.shape[1]), (255, 255, 0), 20)  # draw a line (image, start point, end point, color, thickness)

# draw an arrow
cv.arrowedLine(colored_img, (200, 200), (400, 400), (0, 255, 255), 10)  # draw a arrowed line (image, start point, end point, color, thickness)

# # draw a rectangle
cv.rectangle(colored_img, (200, 50), (500, 200), (0, 200, 255), 10)  # draw a rectangle (image, start point, end point, color, thickness)

# fill a rectangle
cv.rectangle(colored_img, (200, 50), (500, 200), (0, 200, 255), -1)  # draw a rectangle (image, start point, end point, color, thickness)

# cv.rectangle(colored_img, (200, 50), (500, 200), (0, 200, 255), cv.FILLED)  # draw a rectangle (image, start point, end point, color, thickness)

# # draw a circle
cv.circle(colored_img, (447, 63), 63, (255, 255, 255), -1)  # draw a circle (image, center, radius, color, thickness)

# # draw a polygon
# pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)  # create a array of points
# pts = pts.reshape((-1, 1, 2))  # reshape the array
# img = cv.polylines(img, [pts], True, (0, 255, 255), 3)  # draw a polygon (image, points, isClosed, color, thickness)

# # write text
font = cv.FONT_HERSHEY_SIMPLEX  # create a font
cv.putText(colored_img, 'OpenCV', (10, 500), font, 2, (255, 255, 0), 3, cv.LINE_AA)  # write text (image, text, start point, font, fontScale, color, thickness, lineType)

# cv.imshow("Image", img)  # display image
# cv.imshow("Image1", img1)  # display image
cv.imshow("Colored Image", colored_img)  # display image

cv.waitKey(0)  # wait for any key to exit
cv.destroyAllWindows()  # destroy all windows
