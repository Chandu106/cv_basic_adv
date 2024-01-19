import cv2 as cv 
import numpy as np

img = cv.imread("/home/chandu/cv_ws/Resources/Photos/park.jpg")
cv.imshow("image", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("blank", blank)

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

merged_image = cv.merge([b, g, r])
cv.imshow("merged_image", merged_image)

cv.waitKey(0)