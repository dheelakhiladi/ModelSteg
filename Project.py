import binascii as ba
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
image=cv.imread('/home/hitman/Documents/Study/Sem7/PBL(s)/InformationSecurity/Lenna.png',cv.CV_LOAD_IMAGE_GRAYSCALE)
with open ("/home/hitman/Documents/WORK/Development/Development/ISP/data.txt","r") as file:
	label=file.read()
	label=label[:-1]
bintext=bin(int(ba.hexlify(label),16))
bintext=bintext[2:]
for i in range(image.shape[0]):
	for j in range (image.shape[1]):
		print bin(image[i][j])[2:]
cv.imshow('Lena',image)
cv.waitKey(0)
cv.destroyAllWindows()