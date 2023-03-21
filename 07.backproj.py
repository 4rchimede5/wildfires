import cv2 as cv
import numpy as np

roi = cv.imread('') red rose
hsv = cv.cvtColor(roi,COLOR_BRG2HSV)

target = cv.imread('') rose
hsvt = cv.cvtColot(target,cv.COLOR_BGR2HSV)

roihist = cv.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

cv.normalize(roihist,roihist,0,255,cv.NORM_MINMAX)
dst = cv.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
cv.filter2D(dst,-1,disc,dst)

ret, thresh = cv.threshold(dst,50,255,0)
thresh = cv.merge((thresh,thresh,thresh)
res = cv.bitwise_and(target,thresh

res = n.vstack((targt,thresh,res))
cv.imwrite(''res)
