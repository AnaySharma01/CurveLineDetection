# Imports necessary packages
import cv2 as cv
import numpy as np

def processImage(image):
    # Applies gaussian blur, median blur, and canny edge detection on the image
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Lines 35-38
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 1)
    median_blur = cv.medianBlur(gray_scale, 5)
    #https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Line 36
    canny_image = cv.Canny(median_blur, 25, 25)

    # Creates a mask around desired area
    # https://pyimagesearch.com/2021/01/19/image-masking-with-opencv/ Lines 20-26
    roi = np.zeros(image.shape[:2], dtype="uint8")
    cv.rectangle(roi, (20, 20), (400, 400), 1, -1)
    mask = cv.bitwise_and(canny_image, canny_image, mask=roi)
    # Displays the mask
    cv.rectangle(image, (20, 20), (400, 400), (255, 0, 0), 5)
    #Creates the contours
    #https://www.geeksforgeeks.org/find-and-draw-contours-using-opencv-python/
    contour = contours, hierarchy = cv.findContours(mask,
                                           cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # Prevents program from crashing if no lines detected
    #https://www.tutorialspoint.com/how-to-compute-image-moments-in-opencv-python
    if contour is not None:
        #Displays the lines
        cv.drawContours(image, contours, -1, (255, 0, 0), 5)

        #https://www.tutorialspoint.com/how-to-compute-image-moments-in-opencv-python Example 2
        for i, line1 in enumerate(contours):
            for j, line2 in enumerate(contours):
                x1, y1 = line1[0, 0]
                x2, y2 = line2[0, 0]
                cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 5)
                # Calculates and displays the centerline
                cv.line(image, ((x1 + x2)//2, (y1 + y2)//2), ((x2 + x1)//2, (y2 + y1)//2), (0, 255, 0), 5)
