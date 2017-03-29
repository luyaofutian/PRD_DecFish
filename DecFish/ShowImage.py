# -*- coding: cp936 -*-
import cv2
from Tkinter import *
import tkMessageBox
import sys
import urllib2
import cv2
import numpy as np
import math
import tkFileDialog

class ShowImage():

    def get_image(self):
        '''
        Create the function to open the path dialog box and select the image
        :return:
        '''
        global src_img
        # getting the image address
        fname = tkFileDialog.askopenfilename()
        print fname
        img = cv2.imread(fname);
        src_img = img
        # root.mainloop()

