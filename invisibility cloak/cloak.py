import cv2 
import time
import numpy as np 

# preparing code to see video output 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outputfile = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# using video capture function 
cap = cv2.VideoCapture(0)
# warming up the camera
time.sleep(2)
bg = 0 
# capturing background in the range of 60 frames
for i in range(60):
    ret, bg = cap.read()
    
# flip background
bg = np.flip(bg)

# read captured plan while it is open
while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    img = np.flip(img, axis=1)
    # ret returns true or false
    # converting bgr to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # creating mask to check for the color in specified range
    lowerRed = np.array([0, 120, 50])
    upperRed = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lowerRed, upperRed)
    lowerRed = np.array([170, 120, 70])
    upperRed = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lowerRed, upperRed)
    mask1 = mask1 + mask2
    # morphology accepts the params of the source
    # using morphologyex method 
    # uint => integer upto 255
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))
    # mask to segment out the red
    # selecting thep part that does not have the mask 
    mask2 = cv2.bitwise_not(mask1)
    # creating two resolutions 
    # keeps the part without red color 
    res1 = cv2.bitwise_and(img, img, mask=mask2)
    # keeps the part with red color
    res2 = cv2.bitwise_and(bg, bg, mask=mask1)
    # generate the final video 
    finaloutput = cv2.addWeighted(res1, 1, res2, 1, 0)
    outputfile.write(finaloutput)
    # display out put 
    cv2.imshow("magic", finaloutput)
    cv2.waitKey(1)
# hsv, saturation and value

cap.release()
cv2.destroyAllWindows()
