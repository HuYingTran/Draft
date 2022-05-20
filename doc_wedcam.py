import cv2
import os

camera_id = 0
cap =cv2.VideoCapture(camera_id)
while True:
    ret, frame = cap.read()
    cv2.imshow("Cam",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # SPACE pressed
        cv2.imwrite("anhchup.jpg", frame)
        break
del(cap)

img = cv2.imread("anhchup.jpg")
cv2.imshow("anh",img)
os.remove("anhchup.jpg")

cv2.waitKey(0)