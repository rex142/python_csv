
import cv2

url = "005-005-005-01020240527035223665569.mp4"


capture = cv2.VideoCapture(url)
while True:
    grabbed, frame = capture.read()
    if grabbed:
        cv2.imshow("frame", frame)
        cv2.waitKey(10)
capture.release()
cv2.destroyAllWindows()
