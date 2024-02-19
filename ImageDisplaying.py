#Imports necessary packages
import cv2 as cv

def displayImage(image):
    #Returns the processed frame
    #https://www.geeksforgeeks.org/python-play-a-video-using-opencv/ lines 20 - 23
    cv.imshow("Detected Lines", image)
    cv.waitKey(1)
