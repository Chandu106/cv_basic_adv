import cv2 as cv 

# for reading the video

capture = cv.VideoCapture("/home/chandu/cv_ws/Resources/Videos/dog.mp4")

haar_cascade = cv.CascadeClassifier("/home/chandu/cv_ws/haar_cascade_face.xml")

# for reading the web cam from the laptop/computer

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=2)
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

    cv.imshow("video", frame)

    print("Number of faces found: " + str(len(faces_rect)))

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()




