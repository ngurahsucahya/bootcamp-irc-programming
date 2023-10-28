import cv2
import torch
import yolov5

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    results = model(frame)

    results.render()
    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
