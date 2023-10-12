import cv2
import time
import numpy as np

#To save the output in a file output.avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

#Starting the webcam
cap = cv2.VideoCapture(0)

#Allowing the webcam to start by making the code sleep for 2 seconds
time.sleep(2)
bg = 0

#Capturing background for 60 frames
for i in range(60):
    ret, bg = cap.read()
#Flipping the background
bg = np.flip(bg, axis=1)

#Reading the captured frame until the camera is open
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    #Flipping the image for consistency
    img = np.flip(img, axis=1)


    hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,120,50])
    upper_red = np.array([10, 255 , 255])

    mask1 = cv2.inRange(hsv, lower_red,upper_red)

    lower_red = np.array([170,120,70])
    upper_red = np.array([180, 255 , 255])

    mask2 = cv2.inRange(hsv, lower_red,upper_red)

    mask1= mask1+mask2





    #Generating the final output
    final_output = img
    output_file.write(img)
    #Displaying the output to the user
    cv2.imshow("magic", mask1)

    cv2.imshow("Masking", mask2)
    cv2.waitKey(1)


cap.release()
out.release()
cv2.destroyAllWindows()

