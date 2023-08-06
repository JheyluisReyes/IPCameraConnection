import cv2

camera = cv2.VideoCapture("rtsp://user:***root@127.0.0.1/video")

while True:
    ret, frame = camera.read()
    cv2.imshow('capture', frame)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()