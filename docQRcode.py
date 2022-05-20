import cv2
from pyzbar.pyzbar import decode


camera_id = 0
cap =cv2.VideoCapture(camera_id)
tmp = ""
while True:
    ret, frame = cap.read()
    cv2.imshow("Cam",frame)
    result = decode(frame)
    if result:
        for i in result:
            dulieu = i.data.decode("utf-8")
        if dulieu != tmp:
            print(tmp)
            tmp = dulieu
            print(dulieu)
    else:
        tmp =""
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # SPACE pressed
        break
del(cap)

cv2.waitKey(0)