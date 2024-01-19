import cv2 as cv

#rescaling and resizing the images and videos

def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale) 
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("/home/chandu/cv_ws/Resources/Videos/dog.mp4")


while True:
    isTrue, frame = capture.read()


    frame_resized = rescale_frame(frame)
    cv.imshow("video", frame)
    cv.imshow("resized_video", frame_resized)


    if cv.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)