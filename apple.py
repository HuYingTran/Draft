import cv2
import numpy as np
import time

def drawing(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh_binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(thresh_binary,kernel,iterations = 1)
    erosion = cv2.erode(dilation,kernel,iterations = 6)
    img_r = cv2.dilate(erosion,kernel,iterations = 1)
    
    canny = cv2.Canny(img_r, 30, 30)
    cnts, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img_r, cnts, 0, (0, 255, 0), 10)
    if len(cnts) > 0:
        for cnt in cnts:
                ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                x = int(x)
                y = int(y)
                r = int(radius)
                img = cv2.rectangle(image,(x-r,y-r),(x+r,y+r),(255,0,0),2)
        cv2.imshow("kq",image)

image = cv2.imread("E:\\HocTap\\xla\\apple.jpeg")
scale = 500/image.shape[0]
h=int(image.shape[0]*scale)
w=int(image.shape[1]*scale)
image = cv2.resize(src=image, dsize=(w,h))

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
min_mau_r1 = np.array([0, 120, 100])  # red1
max_mau_r1 = np.array([10, 255, 255])

min_mau_r2 = np.array([160, 100, 50])  # red2
max_mau_r2 = np.array([179, 255, 250])

mask_r1 = cv2.inRange(hsv_img, min_mau_r1, max_mau_r1)
mask_r2 = cv2.inRange(hsv_img, min_mau_r2, max_mau_r2)

mask_r = cv2.bitwise_or(mask_r1,mask_r2)

final_r = cv2.bitwise_and(image,image, mask=mask_r)

if np.any(final_r):
    drawing(final_r)

cv2.waitKey(0)