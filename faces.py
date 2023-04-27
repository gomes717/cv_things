import cv2
import dlib

cap =  cv2.VideoCapture("nvarguscamerasrc sensor_id=0 ! video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080,format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! appsink")

cv2.namedWindow("c0", cv2.WINDOW_AUTOSIZE)

detector_facial = cv2.CascadeClassifier("/home/gomes/dev/cv/Cascades/haarcascade_frontalface_default.xml")

if cap.isOpened():

    while True:
        ready, img = cap.read()

        (height, width) = img.shape[:2]

        res_img = cv2.resize(img, (640, 480))

        img_gray =cv2.cvtColor(res_img, cv2.COLOR_RGB2GRAY)

        faces = detector_facial.detectMultiScale(img_gray)
        # eyes = detector_eye.detectMultiScale(img_gray, scaleFactor=1.07, minNeighbors=10, minSize=(18, 18), maxSize=(55,55))

        for x, y, w, h in faces:
            cv2.rectangle(res_img, (x, y), (x + w, y + h), (0,255,255), 2)

        # for x, y, w, h in eyes:
        #     cv2.rectangle(res_img, (x, y), (x + w, y + h), (255,0,255), 2)

        cv2.imshow("c0", res_img)

        cv2.waitKey(1)

cap.release()
  
cv2.destroyAllWindows()