import cv2

faceCascade= cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/vishal 2.jpg')  # read image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #convert image into gray scale

faces = faceCascade.detectMultiScale(imgGray,1.1,4) # to detect faces( gray_img , scale factor , minimum_neighbour)

for (x,y,w,h) in faces:  #  loop for faces
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)   # create bounding box around the faces


cv2.imshow("Result", img)
cv2.waitKey(0)