import cv2
from random import randrange

# Loading some pre-trained data on the face frontal from opencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choosing an image to detect the face
img = cv2.imread('RDJ2.jpeg')


# Reading the current frame

# Gray scaling the image
gray_scaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(gray_scaled_img)

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)

    # Display img with faces
    cv2.imshow("Face Detection", img)
    cv2.waitKey()

cv2.imshow("Face Detection", img)
key = cv2.waitKey(1)


    # Detect faces
    # face_coordinates = trained_face_data.detectMultiScale(gray_scaled_img)

# print(face_coordinates)
# Draw rectangles around the faces