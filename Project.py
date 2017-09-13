import cv2.cv as cv
image=cv.LoadImage('home/hitman/Desktop/ocv',cv.CV_LOAD_IMAGE_COLOR)
cv.NamedWindow('a_window',cv.CV_WINDOW_AUTOSIZE)
cv.showIMAGE('a_window',image)
cv.waitkey(0)