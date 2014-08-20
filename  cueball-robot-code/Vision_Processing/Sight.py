import cv2, math
import numpy as np
from cv2 import *
f = 'c.jpg'
img = imread(f)
gray = imread(f, 0)

def a(img, gray):

    circles = 5
    blur = GaussianBlur(gray, (5, 5), 2, 2)
    ret,thresh = threshold(gray, 200, 100, THRESH_BINARY)
    circles = HoughCircles(thresh, cv.CV_HOUGH_GRADIENT, 100, 10, circles, 1, 10)
    print circles
    #HCirc not work
    for c in circles[0]:
        circle(img, (c[0], c[1]), c[2], 100)
        circle(img, (c[0], c[1]), 3, (0, 255, 0))
    imshow('img', img)
    waitKey(0)
    destroyAllWindows()

def b(img, gray):
    ret,thresh = threshold(gray, 200, 1, THRESH_BINARY)
    contours,h = findContours(thresh, RETR_EXTERNAL, CHAIN_APPROX_NONE)
    for cnt in contours:
        approx = approxPolyDP(cnt,0.01*arcLength(cnt,False),False)
        approx = approxPolyDP(cnt,0.01*arcLength(cnt,True),True)
        print len(approx)
        if len(approx) < 4:
            drawContours(img, [cnt], 0, 255, 1)
    imshow('img', thresh)
    imshow('img2', img)
    waitKey(0)
    destroyAllWindows()

b(img, gray)
