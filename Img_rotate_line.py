#!/usr/bin/env python3

import cv2
import numpy as np
import imutils

# Đường dẫn ảnh, các bạn đổi tên file tại đây để thử nhé
img_path = "/Users/abc/Documents/Code_doAn/YOLOv5/data_test/0B18DCDT100BS.png"
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Canny = cv2.Canny(gray, 100, 200)
try:
	angles = []
	lines = cv2.HoughLines(Canny, rho=1, theta=np.pi/180, threshold=100)
	for line in lines:
		rho, theta = line[0]
		a = np.cos(theta)
		b = np.sin(theta)
		x0 = a*rho
		y0 = b*rho
		x1 = int(x0 + 1000*(-b))
		y1 = int(y0 + 1000*(a))
		x2 = int(x0 - 1000*(-b))
		y2 = int(y0 - 1000*(a))
		cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
		angles.append((y1 - y2) / (x1 - x2) * (180 / np.pi))
	angle = sum(angles) / len(angles)
	print("góc nghiêng {}".format(angle))
except:
	angle = 0
	
	
def main():	
	Ivehicle = imutils.rotate(img, angle= angle) # hàm xoay ảnh
	cv2.imshow("Img original", img)
	cv2.imshow("Img clean", Ivehicle)
	cv2.waitKey()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()