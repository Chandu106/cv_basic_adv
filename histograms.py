import cv2 as cv 
import matplotlib.pyplot as plt 

img = cv.imread("/home/chandu/cv_ws/Resources/Photos/cats 2.jpg")
cv.imshow("image", img) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#histograms provide the pixel intensity of the image
#grayscale histograms 
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])


plt.figure()
plt.title("Gray_scale histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# colour histograms 

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.title("color histogram")
    plt.xlabel("Bins")
    plt.ylabel("Number of pixels")
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.show()
    

cv.waitKey(0)