import cv2 as cv 

img = cv.imread("/home/chandu/cv_ws/Resources/Photos/park.jpg")
cv.imshow("image", img)

#bgr to gray 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#bgr to hsv 
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

#bgr to lab 
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

#hsv to gray  --> hsv to bgr --> bgr to gray 
#hsv to bgr 
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv_bgr", hsv_bgr)

cv.waitKey(0)