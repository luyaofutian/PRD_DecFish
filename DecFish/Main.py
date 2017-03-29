# -*- coding: cp936 -*-
import cv2
from Tkinter import *
import tkMessageBox
import sys
import urllib2
import cv2
import numpy as np
import math

from ShowImage import ShowImage
from Algorithm import Algorithm


class Main():
    def __init__(self):

        def center_window(root, width, height):
            '''
             creating the center_window function
            :param root: the main root
            :param width: the width of center_window
            :param height: the height of center_window

            '''
            screenwidth = root.winfo_screenwidth()
            screenheight = root.winfo_screenheight()
            size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            print(size)
            root.geometry(size)

        root = Tk()
        # Create the object Tk
        root.title("find fish")
        center_window(root, 500, 440)

        objectA = Algorithm()
        objectS = ShowImage()

        def open_image():
            # Create open_image and call fish_show.py)
            objectS.get_image()

        def haarback():
            # Create a haarback function that calls the haar_check function of algorithm.py
            objectA.haar_check()

        def hogback():
            # Create the hogback function and call the hog_check function
            objectA.hog_check()

        def surfback():
            # Create the surfback function and call the surf_check function
            objectA.surf_check()

        def siftback():
            ##Create the siftback function and call the sift_check()function
            objectA.sift_check()

        def callshow():
            # Create the function callshow () to print help information
            print("1.about this py:write for found fish in picture!\n 2.have any question please the txt 'readme.txt' ")

        """
        创建Button按钮、并设置width，height,relief,bg,bd,fg,state,bitmap,command,anchor
        """
        Button(root, text="open_image", fg="blue", bd=2, width=28, command=open_image).pack()

        Button(root, text="haar_check", fg="blue", bd=2, width=28, command=haarback).pack()

        Button(root, text="hog_check", fg="blue", bd=2, width=28, command=hogback).pack()

        Button(root, text="sift_check", fg="blue", bd=2, width=28, command=siftback).pack()

        Button(root, text="surf_check", fg="blue", bd=2, width=28, command=surfback).pack()
        Button(root, text="help", fg="blue", bd=2, width=28, command=callshow).pack();

        root.mainloop()
main=Main()







