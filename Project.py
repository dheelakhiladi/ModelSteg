import binascii as ba
import cv2 as cv
import numpy as np 
import sys
from matplotlib import pyplot as plt

def longestSubstringFinder(string1, string2):
    answer = ""
    start=0
    count=0
    global end
    global stj
    
    len1, len2 = len(string1), len(string2)
    for i in range(len1):

        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
                count=count+1
            else:
                if (len(match) > len(answer)): 
                	answer = match
	                start=i
	                end=j
	    	match=""
    
    
    stj=end-len(answer)
    print "Index of starting pattern"
    print end-len(answer)
    print "Index of end"
    print end
    print "index of pattern start in image"
    return start
def findfirst1(string1):
	for i in range (len(string1)):
		if(string1[i]=='1'):
			return i;
		else:
			pass
def findfirst0(string1):
	for i in range (len(string1)):
		if (string1[i]=='0'):
			return i
		else:
		 pass


def RLE(string1):
	count=0
	curr=string1[0]
	for i in range(len(string1)):
		if string1[i]==curr:
			count=count+1
		else:
			print count,
			curr=string1[i]
			count=1
	return count

		
image=cv.imread('/home/hitman/Documents/Study/Sem7/PBL(s)/InformationSecurity/Lenna.png',cv.CV_LOAD_IMAGE_GRAYSCALE)
with open ("/home/hitman/Documents/WORK/Development/Development/ISP/data.txt","r") as file:
	label=file.read()
	label=label[:-1]
bintext='{0:08b}'.format(int(ba.hexlify(label),16))

binstr=""
for i in range(image.shape[0]):
	for j in range (image.shape[1]):
		binstr=binstr+'{0:08b}'.format(image[i][j])
print"following is the binary conversion of the string"
print bintext
#print "The following section gives the longest matching pattern of the string and the image"
#print "First line is starting index of the pattern of string"
#print "Second line is ending index"
#print "Third line is starting index in the image"
print longestSubstringFinder(binstr,bintext)
print "address of first encountring 0"
print findfirst0(binstr)
print "address of first encountring 1"
print findfirst1(binstr)
print "This is the run length coding of prefix"
print RLE(bintext[0:stj])
print "This is the run length encoding of the suffix"
print RLE(bintext[end:len(bintext)])
cv.imshow('Lena',image)
cv.waitKey(0)
cv.destroyAllWindows()