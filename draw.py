import cv2 as cv
import numpy as np 

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("Blank", blank)

#1. point the image a certain color

blank[:] = 0,255,0
cv.imshow("green", blank)

blank[:] = 255,0,0
cv.imshow("blue", blank)

blank[:] = 0,0,255
cv.imshow("red", blank)

#2. drawing the rectangle

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow("rectangle", blank)

#3. drawing a circle

cv.circle(blank, (255,255), 40, (255,255,255), thickness=2)
cv.imshow("circle", blank)

#4. drawing a line

cv.line(blank, (0,0), (255,255), (255,100,0), thickness=2)
cv.imshow("line", blank)

#5. writing the text 

cv.putText(blank, "Chandu", (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (150,200,150), 3)
cv.imshow("text", blank)

cv.waitKey(0)