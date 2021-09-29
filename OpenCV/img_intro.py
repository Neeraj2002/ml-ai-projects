import cv2

img = cv2.imread('C:/Users/nnr07/PycharmProjects/ML-AI-NN/ML-AI/OpenCV/assets/immg.jpeg', 1)
# -1 => cv2.IMREAD_COLOR: Loads a color image. Any transparency of imagek
# 0 => cv2.IMREAD_GRAYSCALE: Loads image in grayscale mode
# 1 => cv2.IMREAD_UNCHANGED: Loads image as such including alpha channel

# RESIZING THE IMAGE
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# ROTATING THE IMAGE
# img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)


# CREATING A NEW FILE AND SAVING IT WITH CHANGES
cv2.imwrite('img.jpg', img)

cv2.imshow('picture', img)

# It will wait for infinite amount of time since zero is passed in the waitKey
# The program will wait the number of seconds which is passed after the waitKey( ) and then run the next line
cv2.waitKey(0)


cv2.destroyAllWindows()