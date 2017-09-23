import binascii as ba
import cv2 as cv
import numpy as np 
import sys
from matplotlib import pyplot as plt
def longestSubstringFinder(string1, string2):
    answer = ""
    start=0
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): 
                	answer = match
	                start=i
	    
    		match=""
    
    return start

image=cv.imread('/home/hitman/Documents/Study/Sem7/PBL(s)/InformationSecurity/Lenna.png',cv.CV_LOAD_IMAGE_GRAYSCALE)
with open ("/home/hitman/Documents/WORK/Development/Development/ISP/data.txt","r") as file:
	label=file.read()
	label=label[:-1]
bintext='{0:08b}'.format(int(ba.hexlify(label),16))

binstr=""
for i in range(image.shape[0]):
	for j in range (image.shape[1]):
		binstr=binstr+'{0:08b}'.format(image[i][j])
print longestSubstringFinder(binstr,bintext)
cv.imshow('Lena',image)
cv.waitKey(0)
cv.destroyAllWindows()