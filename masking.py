import cv2 as cv 
import numpy as np 

img = cv.imread("/home/chandu/cv_ws/Resources/Photos/cat.jpg")
cv.imshow("image", img) 

blank = np.zeros(img.shape[:2], 'uint8')
cv.imshow("blank", blank)

mask = cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2) ,blank.shape[0] // 4, 255, -1)
cv.imshow("mask", mask)

masked_img = cv.bitwise_and(img, img, mask = mask)
cv.imshow("masked", masked_img)

cv.waitKey(0)