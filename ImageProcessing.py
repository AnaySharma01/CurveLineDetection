# Imports necessary packages
import cv2 as cv
import numpy as np
def processImage(image):
    # Applies gaussian blur, median blur, and canny edge detection on the image
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Lines 35-38
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 0)
    median_blur = cv.medianBlur(gray_scale, 5)
    #https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Line 36
    dilation = cv.dilate(median_blur, kernel=np.ones((2, 2), np.uint8))
    canny_image = cv.Canny(dilation, 50, 50)

    # Creates a mask around desired area
    # https://pyimagesearch.com/2021/01/19/image-masking-with-opencv/ Lines 20-26
    roi = np.zeros(image.shape[:2], dtype="uint8")
    cv.rectangle(roi, (200, 200), (850, 850), 1, -1)
    mask = cv.bitwise_and(canny_image, canny_image, mask=roi)
    # Displays the mask
    cv.rectangle(image, (200, 200), (850, 850), (255, 0, 0), 5)
    #Creates the contours
    #https://www.geeksforgeeks.org/find-and-draw-contours-using-opencv-python/
    contour = contours, hierarchy = cv.findContours(mask,
                                           cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # Prevents program from crashing if no lines detected
    if contour is not None:
        # Displays the lines
        cv.drawContours(image, contours, -1, (0, 0, 255), 15)
