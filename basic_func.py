import cv2 as cv
img = cv.imread("/home/chandu/cv_ws/Resources/Photos/park.jpg")
cv.imshow("park", img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# blurring the image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

# edge detection
canny = cv.Canny(blur, 200, 225)
cv.imshow("edge", canny)

#dilating the image 
dilated = cv.dilate(canny, (5,5), iterations=3)
cv.imshow("dilated", dilated)

#errdong the image
erroded = cv.erode(dilated, (5,5), iterations=3)
cv.imshow("erode", erroded)

#resizing the image
#interpolation techoniques are useful when we are shrinking and explanding the images
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("resized_img", resize)

#cropping the image
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)