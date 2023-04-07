
import cv2
import numpy as np

# Load the image
img = cv2.imread('leaf.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to obtain a binary image
_, thresh = cv2.threshold(gray, -1, 300, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find the contours in the binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Calculate the area and perimeter of the leaf using the contours
area = cv2.contourArea(contours[0])
perimeter = cv2.arcLength(contours[0], True)

# Display the results
print("Area: ", area)
print("Perimeter: ", perimeter)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
