import cv2 
import numpy as np 
import time 

capture_video = cv2.VideoCapture(0) 

time.sleep(2)  
count = 0 
background = 0

for i in range(60): 
    return_val, background = capture_video.read() 

while (capture_video.isOpened()): 
    return_val, img = capture_video.read() 
    if not return_val : 
        break

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  
  
    lower_red = np.array([90,40,50])
    upper_red = np.array([130,255,255])
    mask1 = cv2.inRange(hsv, lower_red,upper_red)
    
    lower_red = np.array([0,40,50])
    upper_red =  np.array([10,255,255])

    mask2 = cv2.inRange(hsv,lower_red,upper_red)

    mask1 = mask1 + mask2 
  
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8), iterations = 2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,np.ones((3,3),np.uint8), iterations = 1)

    mask2 =cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask = mask1) 
    res2 = cv2.bitwise_and(img, img, mask = mask2) 
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0) 
  
    cv2.imshow("Invisible cloak", final_output) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break


capture_video.release()
cv2.destroyAllWindows()