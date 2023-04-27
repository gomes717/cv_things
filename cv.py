import cv2

img = cv2.imread("./imgs/Lenna256g.png")

(height, width) = img.shape[:2]

res = cv2.resize(img, (int(width * 2), int(height * 2)))

cv2.imshow("orig", img)
cv2.imshow("resized", res)
  
# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)
  
# closing all open windows
cv2.destroyAllWindows()