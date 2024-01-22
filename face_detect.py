import cv2 as cv 

img = cv.imread("/home/chandu/cv_ws/Resources/Photos/group 1.jpg")
cv.imshow("image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

haar_cascade = cv.CascadeClassifier("/home/chandu/cv_ws/haar_cascade_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

print("Number of faces found: " + str(len(faces_rect)))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow("Face_detected", img)

cv.waitKey(0)