import cv2

#tao doi tuong CascadeClassifier, bi loi nen canf them duong dan cv2.data.haarcascades +
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

#doc anh
image = cv2.imread("E:\\Download_Anh\\anhThe3x4.jpg")
#chuyen sang anh xam
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#tim guong mat
faces = face_cascade.detectMultiScale(image_gray,scaleFactor = 1.05,minNeighbors = 5)

#ve hinh chu nhat voi toa do lay trong thu vien face
for x,y,w,h in faces:
    image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
    resized = cv2.resize(image,(int(image.shape[1]/5),int(image.shape[0]/5)))

cv2.imshow("anh",resized)
cv2.waitKey(0)
