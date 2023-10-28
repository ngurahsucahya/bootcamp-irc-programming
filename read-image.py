import cv2 as cv

img: object = cv.imread('3.jpg')

cv.imshow('saya', img)

cv.waitKey(2000)
cv.destroyAllWindows()