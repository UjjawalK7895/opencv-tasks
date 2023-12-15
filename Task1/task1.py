import cv2
import numpy


f = open('Detected.txt', 'w')

img = cv2.imread("images/image.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,50,255,0)

contours,hierarchy = cv2.findContours(thresh, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)


for i in contours:


    approx = cv2.approxPolyDP(i, 0.01*cv2.arcLength(i, True), True)
    M = cv2.moments(i)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.drawContours(img, [i], -1, (0, 255, 0), 2)
    cv2.circle(img, (cx, cy), 4, (0, 0, 255), -1)
    

    polygon = ""

    if(len(approx) == 3):
       polygon = "triangle"
    elif(len(approx) == 4):
       polygon = "square"
    elif(len(approx) == 6):
       polygon = "hexagon"
    
    f.write(f"Polygon: {polygon} x: {cx} y: {cy}\n")

f.close()

cv2.imshow("Polygons", img)

cv2.waitKey(0);

cv2.destroyAllWindows;