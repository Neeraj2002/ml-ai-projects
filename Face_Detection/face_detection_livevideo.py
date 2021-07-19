import cv2
from random import randrange

# Loading some pre-trained data on the face frontal from opencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choosing an image to detect the face
"""img = cv2.imread('RDJ2.jpeg')"""
webcam = cv2.VideoCapture(0)

# Iterating over the frames
while True:

    # Reading the current frame
    success_frame_read, frame = webcam.read()

    # Gray scaling the image
    gray_scaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(gray_scaled_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)

        # Display img with faces
        cv2.imshow("Face Detection", frame)
        cv2.waitKey(1)

    cv2.imshow("Face Detection", frame)
    key = cv2.waitKey(1)

    # Program will break if Q key is pressed
    if key == 81 or key == 113:
        break

# Releasing the Video Capture Object
webcam.release()

    # Detect faces
    # face_coordinates = trained_face_data.detectMultiScale(gray_scaled_img)

# print(face_coordinates)
# Draw rectangles around the faces

