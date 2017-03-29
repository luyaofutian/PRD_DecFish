# -*- coding: cp936 -*-
import cv2
from Tkinter import *
import tkMessageBox
import sys
import urllib2
import cv2
import numpy as np
import math
import os
import ShowImage

class Algorithm():
    def __init__(self):
        pass

    def haar_check(self):
        '''
        Create the haar function,using the trained haar classifier (opencv_tarining.exe with opencv ), to detect the object of the picture
        :return:
        '''

        fish_patterns = cv2.CascadeClassifier('haar.xml')
        # Load the trained classifier


        haar_img = ShowImage.src_img
        # Call the src_img image in ShowImage.py
        fish = fish_patterns.detectMultiScale(haar_img, scaleFactor=1.16,
                                              minNeighbors=5, minSize=(50, 60),
                                              maxSize=(150, 150))


        # using the trained haar classifier (opencv_tarining.exe with opencv ), to detect the object of the picture
        # :param  MinNeighbors the parameters  can change the range of 1 to 10, not the same degree of fish-intensive, the smaller the value of the detection of the more
        # param haar_img:Enter the picture  to detect
        # param scaleFactor: Enter the characteristic parameters
        # param minNeighbors:Set the minimum distance (in pixels) for defining the adjacent distance between two detected targets,
        # param minSize:Set to limit the minimum size of  the detection target
        # param maxSize:to limit he maximum size of the detection target

        count = 0
        # Mark the area of the detected fish and display the length and width of the area
        if len(fish) > 0:
            for (x, y, w, h) in fish:

                region = haar_img[x:x + w, y:y + h]
                if (w > 50 and h > 50 and x > 0 and y > 0 and (w > 100 or h > 100)):
                    # To obtain the detected area, and then use the traditional function for further screening
                    count = count + 1
                    cv2.rectangle(haar_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

                    # Write the length and width of the target found on the current graph
                    cv2.putText(haar_img, "w: {}".format(w), (x, y + h),
                                cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 0, 255), 3)
                    cv2.putText(haar_img, "h: {}".format(h), (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 0, 255), 3)
        print(count)
        # Print the number of fish detected
        # import os
        height, width = haar_img.shape[:2]
        size = (int(width * 0.15), int(height * 0.15))
        # Shrink the image, the ratio is (0.2, 0.2)
        shrink = cv2.resize(haar_img, size, interpolation=cv2.INTER_AREA)
        cv2.imshow("haar", shrink)
        # showing the image with the marked dection object
        cv2.imwrite("result/result_haar.jpg", shrink)
        # Save the result graph


    def hog_check(self):
        '''
        Create the hog function, using the trained hog classifier (opencv_tarining.exe with opencv ), to detect the object of the picture
        :return:
        '''

        fish_patterns = cv2.CascadeClassifier('hog.xml')
        # Load the trained classifier
        hog_img = ShowImage.src_img
        # Call the image of src_img in Showimage.py
        fish = fish_patterns.detectMultiScale(hog_img, scaleFactor=1.16,
                                              minNeighbors=10, minSize=(30, 40),
                                              maxSize=(250, 150))
        # using the trained hog classifier (opencv_tarining.exe with opencv ), to detect the object of the picture
        # param  MinNeighbors the parameters  can change the range of 1 to 10, not the same degree of fish-intensive, the smaller the value of the detection of the more
        # param haar_img:Enter the picture  to detect
        # param scaleFactor: Enter the characteristic parameters
        # param minNeighbors:Set the minimum distance (in pixels) for defining the adjacent distance between two detected targets,
        # param minSize:Set to limit the minimum size of  the detection target
        # param maxSize:to limit he maximum size of the detection target
        count = 0
        # Mark the area of the detected fish and display the length and width of the area
        if len(fish) > 0:
            for (x, y, w, h) in fish:

                region = hog_img[x:x + w, y:y + h]
                if (w > 50 and h > 50 and x > 0 and y > 0 and (w > 100 or h > 100)):
                    # To obtain the detected area, and then use the traditional function for further screening
                    count = count + 1
                    cv2.rectangle(hog_img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                    # Write the length and width of the target found on the current graph
                    cv2.putText(hog_img, "w: {}".format(w), (x, y + h),
                                cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 0, 0), 3)
                    cv2.putText(hog_img, "h: {}".format(h), (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 0, 0), 3)
        print(count)
        # Print the number of fish detected
        import os
        height, width = hog_img.shape[:2]
        size = (int(width * 0.2), int(height * 0.2))
        # Shrink the image, the ratio is (0.2, 0.2), is conducive to display
        shrink_hog = cv2.resize(hog_img, size, interpolation=cv2.INTER_AREA)
        cv2.imshow("Image_hog", shrink_hog)
        # The chart marked with the detection target is displayed
        cv2.imwrite("result/result_hog.jpg", shrink_hog)
        # Save the result graph

    def sift_check(self):
        '''
        Create the sift function
        :return:
        '''
        img = ShowImage.src_img
        height, width = img.shape[:2]
        size = (int(width * 0.2), int(height * 0.2))
        # Reduce the image, the ratio is (0.2, 0.2), is conducive to shorten the detection time
        shrink = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(shrink, cv2.COLOR_BGR2GRAY)
        sift = cv2.SIFT(2)
        # 3000 can be adjusted here, will be different results
        kp = sift.detect(gray, None)
        # Kp is the set of all 128 feature descriptors, ie the number of corners detected
        print len(kp)
        shrink = cv2.drawKeypoints(shrink, kp, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow("sift", shrink)
        cv2.imwrite("result/sift.jpg", shrink)

    def surf_check(self):
        '''
        Create the surf function
        :return:
        '''
        surf = cv2.SURF(6000)
        # Detection of the feature point, where the parameters 2000 according to the actual adjustment
        surf_img = ShowImage.src_img
        # Call ShowImage.src_img
        gray = cv2.cvtColor(surf_img, cv2.COLOR_BGR2GRAY)
        # Grayscale processing
        kp,res = surf.detectAndCompute(gray, None)
        # Calculate the surf eigenvalue
        print res.shape
        img1 = cv2.drawKeypoints(surf_img, kp, None, (0, 255, 0), 4)  # The green dot is detected by the surf algorithm
        # Show feature points
        print(len(kp))
        # Prints the number of corners detected
        import os
        height, width = img1.shape[:2]
        size = (int(width * 0.2), int(height * 0.2))
        # Reduce the image, the ratio is (0.2, 0.2), conducive to display
        shrink = cv2.resize(img1, size, interpolation=cv2.INTER_AREA)
        cv2.imwrite("result/SURF.jpg", shrink)
        cv2.imshow("SURF", shrink)
        # Save the test results locally











