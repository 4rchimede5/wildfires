import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('',0)

ret, thr1 = cv.threshold(img,50,255,cv.THRESH_BINARY)
ret, thr2 = cv.threshold(img,50,255,cv.THRESH_BINARY_INV)
ret, thr3 = cv.threshold(img,50,255,cv.THRESH_TRUNC)
ret, thr4 = cv.threshold(img,50,255,cv.THRESH_TOZERO)
ret, thr5 = cv.threshold(img,50,255,cv.THRESH_TOZERO_INV)

titles = ['Original Image', 'Binary', 'Binary Inv', 'TRUNC', 'ToZero', 'ToZero_INV']
images = [img, thr1, thr2, thr3 ,thr4, thr5,]

for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()
