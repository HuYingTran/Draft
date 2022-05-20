import cv2
import numpy as np
import time

# vẽ biên cho quả cà chua
def drawing(img):
    image = cv2.blur(img,(5,5))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh_binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    canny = cv2.Canny(thresh_binary, 30, 30)
    #cv2.imshow("duongBao",canny)
    cnts, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    shape = image.copy()
    cv2.drawContours(shape, cnts, 0, (0, 255, 0), 2)
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))
        radius = int(radius)
        img = cv2.circle(img, center, radius, (255, 0, 0), 3)
        cv2.imshow("kq",img)

# ảnh đầu vào
img = cv2.imread("E:\Download_Anh\anhCaChua1.jpg")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)     # chuyển sang màu HSV

# các ngưỡng màu
min_mau_r1 = np.array([0,100,100])  # red1
max_mau_r1 = np.array([10, 255, 255])

min_mau_r2 = np.array([150, 100, 100])  # red2
max_mau_r2 = np.array([179, 105, 100])

min_mau_g = np.array([40, 100, 100])  # green
max_mau_g = np.array([90, 255, 255])

min_mau_y = np.array([15, 100, 100])  # yellow
max_mau_y = np.array([50, 255, 255])

# tạo các lớp mặt nạ để tách màu
mask_r1 = cv2.inRange(hsv_img, min_mau_r1, max_mau_r1)
mask_r2 = cv2.inRange(hsv_img, min_mau_r2, max_mau_r2)

mask_r = cv2.bitwise_or(mask_r1,mask_r1)

cv2.imshow("anh",mask_r)

mask_g = cv2.inRange(hsv_img, min_mau_g, max_mau_g)

mask_y = cv2.inRange(hsv_img, min_mau_y, max_mau_y)

final_g = cv2.bitwise_and(img,img,mask=mask_g)

final_r = cv2.bitwise_and(img,img, mask=mask_r)

final_y = cv2.bitwise_and(img,img, mask=mask_y)


if np.any(final_r):
    print("1")
    drawing(final_r)
if np.any(final_g):
    print("2")
    drawing(final_g)
if np.any(final_y):
    print("3")
    drawing(final_y)

cv2.waitKey(0)