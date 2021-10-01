import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))  # 3 is for WIDTH
    height = int(cap.get(4))  # 4 is for HEIGHT

    # LINE
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 2)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 2)

    # RECTANGLE
    img = cv2.rectangle(img, (100, 100), (200, 200), (0, 0, 255), -1)

    # CIRCLE
    img = cv2.circle(img, (300, 300), 60, (0, 0, 0), -1)

    # TEXT BOX
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'I am the Best', (200, height - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    #               where, text,           position,       font, font scale, color, thickness, line type

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()