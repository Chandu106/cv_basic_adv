import cv2 as cv 
import numpy as np 

blank = np.zeros((400, 400), 'uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv.imshow("rectangle", rectangle)

circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
cv.imshow("circle", circle)

# bitwise_and operation intersecting
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise_And", bitwise_and)

#bitwise_or operation intersecting and non intersecting
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise_or", bitwise_or)

#bitwise_xor operation non intersecting
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise_xor", bitwise_xor)

#bitwise_not 
bitwise_not_rect = cv.bitwise_not(rectangle)
cv.imshow("bitwise_not_rect",bitwise_not_rect)

bitwise_not_cir = cv.bitwise_not(circle)
cv.imshow("bitwise_not_cir",bitwise_not_cir)

cv.waitKey(0)