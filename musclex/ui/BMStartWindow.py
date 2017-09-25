"""
Copyright 1999 Illinois Institute of Technology

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL ILLINOIS INSTITUTE OF TECHNOLOGY BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this notice, the name of Illinois Institute
of Technology shall not be used in advertising or otherwise to promote
the sale, use or other dealings in this Software without prior written
authorization from Illinois Institute of Technology.
"""

__author__ = 'Jiranun.J'

import sys
import os
from PyQt4 import QtGui
from os.path import split
from musclex.ui.BioMuscleWindow import BioMuscleWindow
import musclex

class BMStartWindow(QtGui.QMainWindow):
    """
    A class for start-up window or main window. Now, this is used for keep all BioMuscleWindow objects in a list
    """
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.dir_path = ""
        self.setWindowTitle("Bio-Muscle v."+musclex.__version__)
        self.windowList = [] # use this list to keep BioMuscleWindow objects to prevent python delete it
        self.browseFile() # start program by browse a file

    # def initUI(self):
    #     QtGui.QApplication.processEvents()
    #     self.centralWidget = QtGui.QWidget(self)
    #     self.mainLayout = QtGui.QGridLayout(self.centralWidget)
    #     self.setCentralWidget(self.centralWidget)
    #
    #     self.selectFileButton = QtGui.QPushButton("Select a File")
    #     self.selectFileButton.setFixedHeight(50)
    #     self.selectFolderButton = QtGui.QPushButton("Select a Folder")
    #     self.selectFolderButton.setFixedHeight(50)
    #     self.mainLayout.addWidget(self.selectFileButton, 0, 0, 1, 1)
    #     # self.mainLayout.addWidget(self.selectFolderButton, 1, 0, 1, 1)
    #
    #     self.resize(500, 100)
    #     self.show()
    #
    # def setConnections(self):
    #     self.selectFileButton.clicked.connect(self.browseFile)
    #     # self.selectFolderButton.clicked.connect(self.browseFolder)

    def childWindowClosed(self, childwin):
        """
        Remove child window from list
        :param childwin: BioMuscleWindow object
        """
        if childwin in self.windowList:
            self.windowList.remove(childwin)

        # If window list is empty, exit the program
        if len(self.windowList) == 0:
            sys.exit()

    # def browseFolder(self):
    #     dir_path = QtGui.QFileDialog.getExistingDirectory(self, "Select a Folder")
    #     if dir_path != "":
    #         imgList = getImgFiles(str(dir_path))
    #         nImg = len(imgList)
    #
    #         if nImg < 1:
    #             errMsg = QtGui.QMessageBox()
    #             errMsg.setText('Process Folder Error')
    #             errMsg.setInformativeText(
    #                 'This is an empty folder. Please select another file or folder.')
    #             errMsg.setStandardButtons(QtGui.QMessageBox.Ok)
    #             errMsg.setIcon(QtGui.QMessageBox.Warning)
    #             errMsg.exec_()
    #             return
    #
    #         errMsg = QtGui.QMessageBox()
    #         errMsg.setText('Process folder')
    #         errMsg.setInformativeText('Are you sure you want to process ' + str(len(imgList)) + ' image(s)? This might take long.')
    #         errMsg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
    #         errMsg.setIcon(QtGui.QMessageBox.Warning)
    #         ret = errMsg.exec_()
    #
    #         if ret == QtGui.QMessageBox.Yes:
    #             print "YEAH!"

    def browseFile(self):
        """
        Popup an input file dialog. Users can select .tif for image or .txt for failed cases list
        """
        file_name = QtGui.QFileDialog.getOpenFileName(self, "Please Select a File for Bio-Muscle v."+musclex.__version__,
                                                      filter='Images (*.tif);;Failed cases (*.txt)')
        _, ext = os.path.splitext(str(file_name))
        _, name = split(str(file_name))
        if file_name != "":
            if ext == ".txt" and not name == "failedcases.txt":
                errMsg = QtGui.QMessageBox()
                errMsg.setText('Invalid Input')
                errMsg.setInformativeText("Please select only failedcases.txt or .tif image\n\n")
                errMsg.setStandardButtons(QtGui.QMessageBox.Ok)
                errMsg.setIcon(QtGui.QMessageBox.Warning)
                errMsg.exec_()
                self.browseFile()
            else:
                # Run BioMuscle if the file is an image .tif or failed cases list
                self.runBioMuscle(str(file_name))
        else:
            sys.exit()

    def runBioMuscle(self, filename):
        """
        Create a BioMuscleWindow object and launch the window
        :param filename: input filename (str)
        :return:
        """
        newWindow = BioMuscleWindow(self, filename)
        self.windowList.append(newWindow)
        self.hide()