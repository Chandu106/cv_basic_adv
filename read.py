import cv2 as cv 

# for reading the image

img = cv.imread("/home/chandu/cv_ws/Resources/Photos/cat.jpg")
cv.imshow("cat", img)

# for reading the video

capture = cv.VideoCapture("/home/chandu/cv_ws/Resources/Videos/dog.mp4")

# for reading the web cam from the laptop/computer

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    cv.imshow("video", frame)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()




