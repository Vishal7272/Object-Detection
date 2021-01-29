import cv2

frameWidth = 640  # frame size of video
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
minArea = 500
color = (255,0,255)

cap = cv2.VideoCapture(0)  # to read video
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # to make gray scale image
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)  # to detect
    for (x, y, w, h) in numberPlates:
        area = w*h  # for filter area(minimum) to detect
        if area >minArea:   # if area is greater then minimum area then detect the NO Plate
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img,"Face",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)  # for lable text on it
            imgRoi = img[y:y+h,x:x+w]  # for region of no. plate
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):  # press "s" for save No. img
        cv2.imwrite("Resources/Scanned/NoPlate_"+str(count)+".jpg",imgRoi)    # to capture No. plate
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count +=1