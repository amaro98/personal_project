# [IMPORTING LIBRARIES]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2


# [MAKE IMG PREPROCESS FUNCTIONS]
'''
  PREPROCESSING INCLUDES:
    1. Converting RGB to Grayscale using cvtColor
    2. Apply Gaussian Blue using GaussianBlur
    3. Outline strongest gradient using Canny
'''


# FUNCTION 1 : ASSIGNING COORDINATES OF THE LINES
def make_coordinate(image,line_parameters):

    '''
    [NOTE!]

    - if we execute: print(image.shape),
        Output:

        [h]  [w] [rgb]
        (704, 1279, 3)
        (704, 1279, 3)


    - y2 = int(y1*(3/5))  means 704*3/5 which mean both line will start at bottom (y = 704) and goes to 3/5 of the way
    - x12 is basically rearranged y = mx + C
    '''

    slope, intercept = line_parameters
    y1 = int(image.shape[0])
    y2 = int(y1*(3/5))
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return [[x1, y1, x2, y2]]



# FUNCTION 2 : CALCULATING SLOPE AND LINE INTERCEPT
def average_slope_intercept(image, lines):
    left_fit    = []
    right_fit   = []
    if lines is None:
        return None
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit         = np.polyfit((x1,x2),
                                    (y1,y2),
                                    1)
            slope       = fit[0]
            intercept   = fit[1]
            if slope < 0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))

    left_fit_average    = np.average(left_fit, axis=0)
    right_fit_average   = np.average(right_fit, axis=0)
    left_line           = make_coordinate(image, left_fit_average)
    right_line          = make_coordinate(image, right_fit_average)
    averaged_lines      = [left_line, right_line]
    return averaged_lines


# FUNCTION 3 : TURN THE IMAGE INTO BLACK IN WHITE AND BOUNDS THE COLOR GRADIENT
def canny(image):
    gray    = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    k1      = 5                                                           # kernel
    k2      = 5
    blur    = cv2.GaussianBlur(gray, (k1, k2), 0)
    canny   = cv2.Canny(blur, 50, 150)

    return canny


# FUNCTION 4 : DISPLAYING THE LINES
def display_lines(image,lines):
    line_image = np.zeros_like(image)                               # line is a 2d array containing line coord, [[x1,y1,x2,y2]], next we need to reshape to 1d array with 4 elements via reshape()
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image,
                        (x1,y1),
                        (x2,y2),
                        (255,0,0),
                        10)                                            # draw line at line image -> coordinate xy1 -> is xy2 -> color -> thickness

    return line_image


# FUNCTION 5 : AREA OF LANE DETECTION
def region_of_interest(image):
                                                                    #Enclosed region is in triangle, the region is defined as numpy array
    height      = image.shape[0]
    polygons    = np.array(
                            [(200,height),(1100,height),(550,250)]) # Define the coordinate of the vertices
    mask        = np.zeros_like(image)                              # create of array zero at same shape of the orresponding array, both will have the same dimension and pixel
    cv2.fillPoly(mask, [polygons], 255)                             # fill mask, the area bounded by the area will be white
    masked_image = cv2.bitwise_and(image,mask)                      # apply mask to the image command

    return masked_image




'''
    [ (!) IMPORTANT DISCLAIMER (!) ]

    Refer line 103 where:
        cv2.fillPoly(mask, [polygons], 255)

    Some tutorials or guide may use code like:
        cv2.fillPoly(mask, polygons, 255)
    You may use whichever suits you but take note on the METHOD below

    [METHOD 1:]

    def region_of_interest(image):

    height = image.shape[0]
    polygons = np.array([
        [(200,height),(1000,height),(500,300)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    return mask

    [METHOD 2]

    def region_of_interest(image):

    height = image.shape[0]
    polygons = np.array(
        [(200,height),(1000,height),(500,300)])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, [polygons], 255)
    return mask

'''



'''
# [IMPORT AND RENDER PICTURE]

image           = cv2.imread('D:\\00 Personal File\\02 MY PERSONAL PROJECT\My Coding Project\Lane Detection\\test_image.jpg')
lane_image      = np.copy(image)
canny_image     = canny(lane_image)
cropped_image   = region_of_interest(canny_image)                  # apply masked region to canny Image
lines           = cv2.HoughLinesP(cropped_image,
                                  2,                               # this is set at precision of 2 px,
                                  np.pi/180,                       # 1 deg = pi/180,
                                  100,                             # threshold - min acceptable vote to detect line
                                  np.array([]),                    # just a placeholder for array
                                  minLineLength= 40,               # acceptable minimum length of line in pixel
                                  maxLineGap=5)                    # acceptable max distance between segmented line in pixel

averaged_lines = average_slope_intercept(lane_image,lines)

line_image      = display_lines(lane_image,averaged_lines)
combo_image     = cv2.addWeighted(lane_image,0.8,
                                  line_image,1,             #sum color image with line image with weight = lane_image*0.8 + line_image*1.0
                                  0.5)                        #gamma

# RENDER PICTURE
cv2.imshow('Image Preprocess',combo_image)
cv2.waitKey(0)                                          # Set delay to 0 if you want to show the picture infinitely
'''






# [IMPORT AND RENDER VIDEO]
cap = cv2.VideoCapture("D:\\00 Personal File\\02 MY PERSONAL PROJECT\My Coding Project\Lane Detection\\test2.mp4")
while(cap.isOpened()):
    _, frame        = cap.read()                                # _, = boolean that currently not interested
    canny_image     = canny(frame)
    cropped_image   = region_of_interest(canny_image)           # apply masked region to canny Image
    lines           = cv2.HoughLinesP(cropped_image,
                                    2,                          # this is set at precision of 2 px,
                                    np.pi / 180,                # 1 deg = pi/180,
                                    100,                        # threshold - min acceptable vote to detect line
                                    np.array([]),               # just a placeholder for array
                                    minLineLength=40,           # acceptable minimum length of line in pixel
                                    maxLineGap=5)               # acceptable max distance between segmented line in pixel

    averaged_lines  = average_slope_intercept(frame, lines)
    line_image      = display_lines(frame, averaged_lines)
    combo_image     = cv2.addWeighted(frame, 0.8,
                                  line_image, 1,
                                  1)

# RENDER VIDEO
    cv2.imshow('Video', combo_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


'''
 [TERMINOLOGY]

   Hough Space
   - Used for Line Detection
'''
