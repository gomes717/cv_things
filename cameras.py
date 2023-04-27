
# import the opencv library
import cv2
  
  
# define a video capture object
c0 = cv2.VideoCapture("nvarguscamerasrc sensor_id=0 sensor_mode=4 ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)NV12, framerate=(fraction)24/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! appsink")
c1 = cv2.VideoCapture("nvarguscamerasrc sensor_id=1 sensor_mode=4 ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)NV12, framerate=(fraction)24/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! appsink")

erosion_size = 7
erode_el = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                       (erosion_size, erosion_size))

dilate_size = 7
dilate_el = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * dilate_size + 1, 2 * dilate_size + 1),
                                       (dilate_size, dilate_size))

if c1.isOpened() and c0.isOpened():
# if c0.isOpened():
    cv2.namedWindow("c0", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("c1", cv2.WINDOW_AUTOSIZE)
    while True:
        ret_val0, img0 = c0.read()
        orig0 = cv2.resize(img0, (850, 480))
        orig0 = cv2.rotate(orig0, cv2.ROTATE_180)
        res0 = cv2.cvtColor(orig0, cv2.COLOR_BGR2GRAY)
        res0 = cv2.adaptiveThreshold(res0,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,21,9)
        res0 = cv2.medianBlur(res0, 3)
        # res0 = cv2.erode(res0, erode_el)
        res0 = cv2.dilate(res0, dilate_el)
        mask0 = cv2.dilate(res0, dilate_el)
        mask0 = cv2.cvtColor(mask0, cv2.COLOR_GRAY2BGR)
        masked_img0 = cv2.bitwise_and(orig0, mask0)
        ret_val1, img1 = c1.read()
        orig1 = cv2.resize(img1, (850, 480))
        orig1 = cv2.rotate(orig1, cv2.ROTATE_180)
        res1 = cv2.cvtColor(orig1, cv2.COLOR_BGR2GRAY)
        res1 = cv2.adaptiveThreshold(res1,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,21,9)
        res1 = cv2.medianBlur(res1, 3)
        # res1 = cv2.erode(res1, erode_el)
        mask1 = cv2.dilate(res1, dilate_el)
        mask1 = cv2.cvtColor(mask1, cv2.COLOR_GRAY2BGR)
        masked_img1 = cv2.bitwise_and(orig1, mask1)
        cv2.imshow('c1',masked_img1)
        cv2.imshow('c0',masked_img0)
        cv2.waitKey(10)
    else:
        print("camera open failed")
  
# After the loop release the cap object
c0.release()
c1.release()
# Destroy all the windows
cv2.destroyAllWindows()