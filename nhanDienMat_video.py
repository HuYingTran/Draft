import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

camera_id = 0
cap =cv2.VideoCapture(camera_id)
while True:
    ret, frame = cap.read()

    image_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(image_gray, scaleFactor = 1.05,minNeighbors=5)

    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),3)

    cv2.imshow("Cam",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destrovAllWindow()