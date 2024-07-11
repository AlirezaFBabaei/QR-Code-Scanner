# Import libraries
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Reading QR from File

# Load the image
img = cv2.imread('name_of_your_file.jpg')

# Decode the QR code
for barcode in decode(img):
    data= barcode.data.decode('utf-8')
    print(data)

# Reading QR from Camera

# Open the webcam
cap = cv2.VideoCapture(0)

# Set width size
cap.set(3, 640)
# Set height size
cap.set(4, 480)

while True:
    success, img = cap.read() 
    for barcode in decode(img):
        data= barcode.data.decode('utf-8')
        print(data)

        # Extract polygon
        points = np.array([barcode.polygon], np.int32)
        points = points.reshape((-1, 1, 2))

        # Draw polygon
        # Image, Points, Closed, Color, Thickness
        cv2.polylines(img, [points], True, (255, 0, 255), 5)

        # Display extracted text
        points2 = barcode.rect
        cv2.putText(img, data, (points2[0], points2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
    
    cv2.imshow('Result', img)
    cv2.waitKey(1)
