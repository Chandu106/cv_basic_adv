import cv2 as cv 
import numpy as np 

img = cv.imread("/home/chandu/cv_ws/Resources/Photos/park.jpg")
cv.imshow("park", img)

# translating the image 
def translate_img(img, x, y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimensions)

# -x left, +x right, -y up, +y down

translated = translate_img(img, 100, 100)
cv.imshow("translated_img", translated)

#rotating the image 
def rotate_img(img, angle, rotpoint = None):
    (height, width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width // 2 , height // 2)
    
    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotmat, dimensions)

rotated = rotate_img(img, 45)
cv.imshow("rotated_img", rotated)

#resizing the image 
resized = cv.resize(img, (500, 500), cv.INTER_CUBIC)
cv.imshow("resized_image", resized)

#flipping the image 
flip_vertical = cv.flip(img, 0)
cv.imshow("flipped_vertically", flip_vertical)

flip_horizontally = cv.flip(img, 1)
cv.imshow("flipped_horizontally", flip_horizontally)

flip_both = cv.flip(img, -1)
cv.imshow("flipped_both", flip_both)

#cropping the image 
cropped_image = img[200:400, 300:400]
cv.imshow("cropped_image", cropped_image)



cv.waitKey(0)

