import cv2 as cv 

img = cv.imread("/home/chandu/cv_ws/Resources/Photos/cats.jpg")
cv.imshow("image", img)

#1. averaging 
average = cv.blur(img, (5,5))
cv.imshow("average", average)

#2. gaussian 
gauss = cv.GaussianBlur(img, (5,5), 0)
cv.imshow("gauss", gauss)

#3. median 
median = cv.medianBlur(img, 5)
cv.imshow("median", median)

#4. bilateral
bilateral = cv.bilateralFilter(img, 5, 30, 25)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)