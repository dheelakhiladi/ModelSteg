import cv2.cv as cv
image=cv.LoadImage('/home/hitman/Desktop/ocv.jpg',cv.CV_LOAD_IMAGE_UNCHANGED)
font= cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 4, 4, 0, 10, 0)
x=image.height/4
y=image.width
cv.PutText(image,"Mohit 20 M",(x,y),font,cv.RGB(255,255,255))
cv.NamedWindow('MohitTheGunda',400*200)
cv.ShowImage('MohitTheGunda',image)
cv.WaitKey(0)