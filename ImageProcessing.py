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
    canny_image = cv.Canny(median_blur, 100, 20)

    # Creates a mask around desired area
    # https://pyimagesearch.com/2021/01/19/image-masking-with-opencv/ Lines 20-26
    roi = np.zeros(image.shape[:2], dtype="uint8")
    cv.rectangle(roi, (200, 200), (850, 850), 1, -1)
    mask = cv.bitwise_and(canny_image, canny_image, mask=roi)
    # Displays the mask
    cv.rectangle(image, (200, 200), (850, 850), (255, 0, 0), 5)

    #Detects the contours
    ##https://www.tutorialspoint.com/opencv_python/opencv_python_image_contours.htm Line 10
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    # Prevents program from crashing if no contours detected
    if len(contours) > 0:
        # Displays the lines
        #https://www.tutorialspoint.com/opencv_python/opencv_python_image_contours.htm Line 15
        cv.drawContours(image, contours, -1, (0, 255, 0), 5)

        #Finds minimum length of contours
        #https://www.geeksforgeeks.org/python-length-of-shortest-string-in-string-list/ Method 1 Line 13
        min_length = min(len(cnt) for cnt in contours)

        #Calculates the average of the contour points
        #https://www.geeksforgeeks.org/numpy-mean-in-python/ Code 2 Line 15
        midpoint_x_arr = np.mean([contour[:, 0, :][:min_length][:, 0] for contour in contours], axis=0).astype(int)
        midpoint_y_arr = np.mean([contour[:, 0, :][:min_length][:, 1] for contour in contours], axis=0).astype(int)

        #Displays the centerline
        #https://www.geeksforgeeks.org/python-opencv-cv2-line-method/ Example 1 Line 33
        for i in range(len(midpoint_x_arr) - 1):
            cv.line(image, (midpoint_x_arr[i], midpoint_y_arr[i]), (midpoint_x_arr[i+1], midpoint_y_arr[i+1]), (0, 0, 255), 5)

