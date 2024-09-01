!pip install opencv-contrib-python
# OR
!pip install opencv-python

import cv2
import numpy as np

face_detector=cv2.CascadeClassifier('.../haarcascade_frontalface_default.xml') # Location of haarcasade frontalface default file

img = cv2.imread('C:/Users/abhis/Downloads/team india.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
results = face_detector.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in results:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
  
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
