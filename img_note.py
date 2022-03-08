#!/usr/bin/env python3

import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8) # tạo nền đen
img1 = cv2.line(img,(150,200),(400,200),(255,0,0),5) # vẽ đừờng thẳng
img2 = cv2.rectangle(img,(100,450),(450,300),(0,255,0),3) # vẽ hình chữ nhật
img3 = cv2.circle(img,(262,100), 63, (100,0,255), 3) # vẽ hình tròn
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Hung Dang',(100,400), font, 2,(200,50,100),2,cv2.LINE_AA)

def main():	
	cv2.imshow('IMG_line', img)
	cv2.waitKey()
	cv2.destroyAllWindows()
	
if __name__ == '__main__':
	main()