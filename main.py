import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound



camera = cv2.VideoCapture(0)


while True:
    ret, frame = camera.read()
    bbox, caption, conf = cv.detect_common_objects(frame)
    output = draw_bbox(frame, bbox, caption, conf)

    cv2.imshow("Temp", output)

    if cv2.waitKey(1) & 0xFF == ord("x"):
        break