import cv2 as cv 
import numpy as np 

img = cv.imread("/home/chandu/cv_ws/Resources/Photos/park.jpg")
cv.imshow("image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# laplasian 
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap)

#sobel 
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow("sobel_x", sobel_x)
cv.imshow("sobel_y", sobel_y)

combined_sobel = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow("combined_sobel", combined_sobel)

#canny 
cany = cv.Canny(gray, 150, 175)
cv.imshow("canny", cany)


cv.waitKey(0)