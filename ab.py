import cv2

# Load the image
img = cv2.imread('images_with_eyeglasses/000152.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the eye detector
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Detect eyes in the grayscale image
eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

# Draw a box around each eye
for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# Display the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
