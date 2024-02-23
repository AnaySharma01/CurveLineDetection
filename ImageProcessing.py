# Imports necessary packages
import cv2 as cv
import numpy as np

def processImage(image):
    # Applies gaussian blur, median blur, and canny edge detection on the image
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Lines 35-38
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 1)
    median_blur = cv.medianBlur(gray_scale, 5)
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Line 36
    canny_image = cv.Canny(median_blur, 25, 25)

    # Creates a mask around desired area
    # https://pyimagesearch.com/2021/01/19/image-masking-with-opencv/ Lines 20-26
    roi = np.zeros(image.shape[:2], dtype="uint8")
    cv.rectangle(roi, (200, 200), (850, 850), 1, -1)
    mask = cv.bitwise_and(canny_image, canny_image, mask=roi)
    # Displays the mask
    cv.rectangle(image, (200, 200), (850, 850), (255, 0, 0), 5)
    # Creates the contours
    # https://www.geeksforgeeks.org/find-and-draw-contours-using-opencv-python/
    contour = contours, hierarchy = cv.findContours(mask,
                                                    cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # Prevents program from crashing if no lines detected
    # https://www.tutorialspoint.com/how-to-compute-image-moments-in-opencv-python
    if contour is not None:
        # Displays the lines
        cv.drawContours(image, contours, -1, (255, 0, 0), 5)

        # https://www.tutorialspoint.com/how-to-compute-image-moments-in-opencv-python Example 2
        for i, point1 in enumerate(contours):
            for j, point2 in enumerate(contours):
                x1, y1 = point1[0, 0]
                x2, y2 = point2[0, 0]
                midpoint1 = (x1 + x2) // 2
                midpoint2 = (y1 + y2) // 2
                # cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 5)
                # Calculates and displays the centerline
                center_dots = cv.line(image, (midpoint1, midpoint2), (midpoint1, midpoint2), (0, 255, 0), 10)

                #https://www.tutorialspoint.com/how-to-draw-polylines-on-an-image-in-opencv-using-python
                points = np.array([[midpoint1,midpoint2],[midpoint1,midpoint2]])
                pts = points.reshape(-1, 1, 2)
                cv.polylines(image, [pts], isClosed=False, color=(0,0,0), thickness = 2)
