# chapter 9 = how to capture a webcamera video

# Step-1 Import libraries
import cv2 as cv
import numpy as np

# Step-2 Read the frames from the webcam
cap = cv.VideoCapture(0) # 0 for default camera

# indicates if the webcamera is opened or not
# if not cap.isOpened():
#     print("Cannot open webcamera")
#     exit()

# read until video is completed
# Step-3 Display frame by frame
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv.imshow("Frame", frame)
        # Press Q on keyboard to  exit
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Step-4 When everything done, release or close easily
cap.release()
# out.release()
cv.destroyAllWindows()




