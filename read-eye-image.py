import cv2

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

image = cv2.imread('1.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor=1.055, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (200, 95, 200), 2)
    cv2.putText(image, 'eyes', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.imshow('Deteksi Mata', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
