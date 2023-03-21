import cv2 as cv
import numpy as np

def space_holder(x):
	pass

background = np.zeros((500,500,3),np.uint8)
cv.namedWindow('converter')

cv.createTrackbar('R','converter',0,255,space_holder)
cv.createTrackbar('G','converter',0,255,space_holder)
cv.createTrackbar('B','converter',0,255,space_holder)

switch = '0: OFF \n1 : ON'
cv.createTrackbar(switch,'converter',0,1,space_holder)

cv.createTrackbar('H','converter',0,179,space_holder)
cv.createTrackbar('S','converter',0,255,space_holder)
cv.createTrackbar('V','converter',0,255,space_holder)

while(1):
	cv.imshow('converter',background)
	k = cv.waitKey(1) & 0xFF
	if k == 27:
		break
	r = cv.getTrackbarPos('R','converter')
	g = cv.getTrackbarPos('G','converter')
	b = cv.getTrackbarPos('B','converter')
	s = cv.getTrackbarPos(switch, 'converter')

	if s == 0:
		background[:]=0
	else:
		background[:250]=[b,g,r]
		hsvback=background[:250]
		hsv=cv.cvtColor(hsvback,40)
		background[250:500]=hsv
		cv.setTrackbarPos('H','converter',hsv.item(10,10,0))
		cv.setTrackbarPos('S','converter',hsv.item(10,10,1))
		cv.setTrackbarPos('V','converter',hsv.item(10,10,2))

cv.destroyAllWindows()
