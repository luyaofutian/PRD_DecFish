# coding: utf-8

import wx
import wx.py.images
import sys
import urllib2
import cv2
import numpy as np
import math

from ShowImage import ShowImage
from Algorithm import Algorithm

########################################################################
# set the file filter
wildcard1 = "All files (*.*)|*.*|" \
            "Python source (*.py; *.pyc)|*.py;*.pyc"
wildcard2 = "Python source (*.py; *.pyc)|*.py;*.pyc|" \
            "All files (*.*)|*.*"


########################################################################
class MyForm(wx.Frame):
    # -------------------------------------------------------------------
    # set the window layout
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, \
                          "MainWindows", \
                          pos=(0, 0), size=(810, 635))
        # def the global variance
        global TxtCfn
        # layout the Frame
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour('white')
        statusBar = self.CreateStatusBar()  # 1 创建状态栏
        toolbar = self.CreateToolBar()  # 2 创建工具栏
        # toolbar.AddSimpleTool(wx.NewId(), wx.py.images.getPyBitmap(),
        #                       "New", "Long help for 'New'")  # 3 给工具栏增加一个工具
        # toolbar.Realize()  # 4 准备显示工具栏
        menuBar = wx.MenuBar()  # 创建菜单栏
        # 创建两个菜单
        menu1 = wx.Menu()
        # menuBar.Append(menu1, "&File")
        # menu2 = wx.Menu()
        # menuBar.Append(menu2, " & Edit")  # 在菜单栏上附上菜单
        menu3 = wx.Menu()
        menuBar.Append(menu3, "Algoritme")
        menu4 = wx.Menu()
        menuBar.Append(menu4, "About")
        # 6 创建菜单的项目
        # menu1.Append(wx.NewId(), "New")
        # menu1.Append(wx.NewId(), "Open")
        #
        # menu1.Append(wx.NewId(), "Save")
        # menuItem = menu1.Append(-1, "& Exit...")
        # menu2.Append(wx.NewId(), "&Copy", "Copy in status bar")
        # menu2.Append(wx.NewId(), "C&ut", "")
        # menu2.Append(wx.NewId(), "Paste", " ")
        # menu2.AppendSeparator()
        # menu2.Append(wx.NewId(), " & Options...", "Display Options")
        menu4.Append(wx.NewId(), "help", " ")
        menu4.Append(wx.NewId(), "close", " ")
        menu3.Append(wx.NewId(), "SIFT", " ")
        menu3.Append(wx.NewId(), "SURF", " ")
        menu3.Append(wx.NewId(), "Haar", " ")
        menu3.Append(wx.NewId(), "HOG", " ")
        self.SetMenuBar(menuBar)

        TxtCfn = wx.TextCtrl(panel, pos=(15, 5), size=(200, 25))
        btnO = wx.Button(panel, label="Open", pos=(225, 5), size=(70, 25))
        # btnS = wx.Button(panel, label="Save", pos=(300, 5), size=(70, 25))
        # Contents = wx.TextCtrl(panel, pos=(15, 35), size=(360, 260),
        #                        style=wx.TE_MULTILINE | wx.HSCROLL)
        # bind the button event
        btnO.Bind(wx.EVT_BUTTON, self.onOpenFile)
        # btnS.Bind(wx.EVT_BUTTON, self.onSaveFile)
        # -------------------------------------------------------------------
        # def [onOpenFile] function of the label [open]button

    def onOpenFile(self, event):
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard=wildcard1,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            tmp = ""
            # paths = dlg.GetPaths()
            paths = dlg.GetPaths()
            # print "You chose the following file(s):"
            for path in paths:
                tmp = tmp + path
            # set the value of TextCtrl[filename]
            TxtCfn.SetValue(tmp)
            # set the value to the TextCtrl[contents]
            file = open(TxtCfn.GetValue())
            # Contents.SetValue(file.read())
            file.close()
        dlg.Destroy()
        # def onSaveFile function

    # def onSaveFile(self, event):
    #     """
    #     Create and show the Save FileDialog
    #     """
    #     dlg = wx.FileDialog(self,
    #                         message="select the Save file style",
    #                         defaultFile="",
    #                         wildcard=wildcard2,
    #                         style=wx.SAVE
    #                         )
    #     if dlg.ShowModal() == wx.ID_OK:
    #         filename = ""
    #         paths = dlg.GetPaths()
    #         # split the paths
    #         for path in paths:
    #             filename = filename + path
    #         # write the contents of the TextCtrl[Contents] into the file
    #         file = open(filename, 'w')
    #         # file.write(Contents.GetValue())
    #         file.close()
    #         # show the save file path
    #         TxtCfn.SetValue(filename)
    #     dlg.Destroy()
    #     # -----------------------------------------------------------------------
objectA=Algorithm()
objectS=ShowImage()

def open_image():

    objectS.get_image()


def haarback():

    objectA.haar_check()


def hogback():

    objectA.hog_check()


def surfback():

    objectA.surf_check()

def siftback():

    objectA.sift_check()

def callshow():

    print("1.about this py:write for found fish in picture!\n 2.have any question please the txt 'readme.txt' ")

##########################################################################
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
