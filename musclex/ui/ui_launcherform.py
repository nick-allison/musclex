# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launcher.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from .pyqt_utils import *

class Ui_LauncherForm(object):
    def setupUi(self, LauncherForm):
        LauncherForm.setObjectName("LauncherForm")
        LauncherForm.resize(800, 600)
        self.listWidget = QListWidget(LauncherForm)
        self.listWidget.setGeometry(QRect(10, 10, 251, 541))
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setTabKeyNavigation(True)
        self.listWidget.setObjectName("listWidget")
        item = QListWidgetItem()
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.NoBrush)
        item.setBackground(brush)
        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QListWidgetItem()
        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QListWidgetItem()
        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QListWidgetItem()
        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QListWidgetItem()
        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        # item = QListWidgetItem()
        # item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        # self.listWidget.addItem(item)
        item = QListWidgetItem()
        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QListWidgetItem()
        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QListWidgetItem()
        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        self.stackedWidget = QStackedWidget(LauncherForm)
        self.stackedWidget.setGeometry(QRect(270, 10, 521, 541))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_0 = QWidget()
        self.page_0.setObjectName("page_0")
        self.textBrowser_0 = QTextBrowser(self.page_0)
        self.textBrowser_0.setGeometry(QRect(0, 0, 521, 541))
        self.textBrowser_0.setOpenExternalLinks(True)
        self.textBrowser_0.setObjectName("textBrowser_0")
        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName("page_1")
        self.textBrowser_1 = QTextBrowser(self.page_1)
        self.textBrowser_1.setGeometry(QRect(0, 0, 521, 541))
        self.textBrowser_1.setOpenExternalLinks(True)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.textBrowser_2 = QTextBrowser(self.page_2)
        self.textBrowser_2.setGeometry(QRect(0, 0, 521, 541))
        self.textBrowser_2.setOpenExternalLinks(True)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.textBrowser_3 = QTextBrowser(self.page_3)
        self.textBrowser_3.setGeometry(QRect(0, 0, 521, 541))
        self.textBrowser_3.setOpenExternalLinks(True)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName("page_4")
        self.textBrowser_4 = QTextBrowser(self.page_4)
        self.textBrowser_4.setGeometry(QRect(0, 0, 521, 541))
        self.textBrowser_4.setOpenExternalLinks(True)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.stackedWidget.addWidget(self.page_4)
        # self.page_5 = QWidget()
        # self.page_5.setObjectName("page_5")
        # self.textBrowser_5 = QTextBrowser(self.page_5)
        # self.textBrowser_5.setGeometry(QRect(0, 0, 521, 541))
        # self.textBrowser_5.setOpenExternalLinks(True)
        # self.textBrowser_5.setObjectName("textBrowser_5")
        # self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName("page_6")
        self.textBrowser_6 = QTextBrowser(self.page_6)
        self.textBrowser_6.setGeometry(QRect(0, 0, 521, 541))
        self.textBrowser_6.setOpenExternalLinks(True)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName("page_7")
        self.textBrowser_7 = QTextBrowser(self.page_7)
        self.textBrowser_7.setGeometry(QRect(0, 0, 521, 541))
        self.textBrowser_7.setOpenExternalLinks(True)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName("page_8")
        self.textBrowser_8 = QTextBrowser(self.page_8)
        self.textBrowser_8.setGeometry(QRect(0, 0, 521, 541))
        self.textBrowser_8.setOpenExternalLinks(True)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.stackedWidget.addWidget(self.page_8)
        self.layoutWidget = QWidget(LauncherForm)
        self.layoutWidget.setGeometry(QRect(10, 560, 781, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.quitButton = QPushButton(self.layoutWidget)
        self.quitButton.setObjectName("quitButton")
        self.horizontalLayout.addWidget(self.quitButton)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.runButton = QPushButton(self.layoutWidget)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        self.testButton = QPushButton(self.layoutWidget)
        self.testButton.setObjectName("testButton")
        self.horizontalLayout.addWidget(self.testButton)

        self.retranslateUi(LauncherForm)
        self.listWidget.setCurrentRow(0)
        self.stackedWidget.setCurrentIndex(0)
        self.listWidget.currentRowChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        self.quitButton.clicked.connect(LauncherForm.close)
        QMetaObject.connectSlotsByName(LauncherForm)

    def retranslateUi(self, LauncherForm):
        _translate = QCoreApplication.translate
        LauncherForm.setWindowTitle(_translate("LauncherForm", "MuscleX Launcher"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("LauncherForm", "X-Ray Viewer"))
        item = self.listWidget.item(1)
        item.setText(_translate("LauncherForm", "Equator"))
        item = self.listWidget.item(2)
        item.setText(_translate("LauncherForm", "Quadrant Folding"))
        item = self.listWidget.item(3)
        item.setText(_translate("LauncherForm", "Projection Traces"))
        item = self.listWidget.item(4)
        item.setText(_translate("LauncherForm", "Scanning Diffraction"))
        # item = self.listWidget.item(5)
        # item.setText(_translate("LauncherForm", "Diffraction Centroids"))
        item = self.listWidget.item(5)
        item.setText(_translate("LauncherForm", "DDF Processor"))
        item = self.listWidget.item(6)
        item.setText(_translate("LauncherForm", "Add Intensities Single Experiment"))
        item = self.listWidget.item(7)
        item.setText(_translate("LauncherForm", "Add Intensities Multiple Experiments"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.textBrowser_0.setMarkdown(_translate("LauncherForm", "**X-Ray Viewer** is a small program used to display tif and h5 files and able to\n"
"play images in a folder (or h5 file) as a video. A second tab shows a selected\n"
"slice or an integrated slice of the image as a graph. "))
        self.textBrowser_0.setHtml(_translate("LauncherForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">X-Ray Viewer</span> is a small program used to display tif and h5 files and able to play images in a folder (or h5 file) as a video. A second tab shows a selected slice or an integrated slice of the image as a graph. <br /><br />See <a href=\"https://musclex.readthedocs.io/en/latest/AppSuite/XRayViewer\"><span style=\" color:#0000ff;\">https://musclex.readthedocs.io/en/latest/AppSuite/XRayViewer</span></a> for details.</p></body></html>"))
        self.textBrowser_1.setMarkdown(_translate("LauncherForm", "The purpose of the **Equator** program is to analyze the equatorial portion of\n"
"muscle X-ray diffraction patterns. "))
        self.textBrowser_1.setHtml(_translate("LauncherForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The purpose of the <span style=\" font-weight:600;\">Equator</span> program is to analyze the equatorial portion of muscle X-ray diffraction patterns. <br /><br />See <a href=\"https://musclex.readthedocs.io/en/latest/AppSuite/Equator\"><span style=\" color:#0000ff;\">https://musclex.readthedocs.io/en/latest/AppSuite/Equator</span></a> for details.</p></body></html>"))
        self.textBrowser_2.setMarkdown(_translate("LauncherForm", "The equator and the meridian of a fiber diffraction pattern divides a pattern\n"
"into four quadrants. You can regenerate a full diffraction pattern by simply\n"
"rotating the summed quadrant. **Quadrant Folding** is a program for generating\n"
"such a quadrant-folded image. "))
        self.textBrowser_2.setHtml(_translate("LauncherForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The equator and the meridian of a fiber diffraction pattern divides a pattern into four quadrants. You can regenerate a full diffraction pattern by simply rotating the summed quadrant. <span style=\" font-weight:600;\">Quadrant Folding</span> is a program for generating such a quadrant-folded image. <br /><br />See <a href=\"https://musclex.readthedocs.io/en/latest/AppSuite/QuadrantFolding\"><span style=\" color:#0000ff;\">https://musclex.readthedocs.io/en/latest/AppSuite/QuadrantFolding</span></a> for details.</p></body></html>"))
        self.textBrowser_3.setMarkdown(_translate("LauncherForm", "**Projection traces** was conceived originally as a program to extract the\n"
"integrated intensity along a layer line in order to identify positions of\n"
"intensity maxima along with their integrated intensities. It also allows\n"
"measurement of the radial width of meridional reflections. "))
        self.textBrowser_3.setHtml(_translate("LauncherForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Projection traces</span> was conceived originally as a program to extract the integrated intensity along a layer line in order to identify positions of intensity maxima along with their integrated intensities. It also allows measurement of the radial width of meridional reflections.<br /><br />See <a href=\"https://musclex.readthedocs.io/en/latest/AppSuite/ProjectionTraces\"><span style=\" color:#0000ff;\">https://musclex.readthedocs.io/en/latest/AppSuite/ProjectionTraces</span></a> for details.</p></body></html>"))
        self.textBrowser_4.setMarkdown(_translate("LauncherForm", "**Scanning diffraction** imaging experiments attempt to determine the\n"
"distribution of diffracting materials such as collagen, myelin, and amyloid\n"
"structures as a function of position in a sample that is raster scanned in a\n"
"microbeam. "))
        self.textBrowser_4.setHtml(_translate("LauncherForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Scanning diffraction</span> imaging experiments attempt to determine the distribution of diffracting materials such as collagen, myelin, and amyloid structures as a function of position in a sample that is raster scanned in a microbeam.<br /><br />See <a href=\"https://musclex.readthedocs.io/en/latest/AppSuite/ScanningDiffraction\"><span style=\" color:#0000ff;\">https://musclex.readthedocs.io/en/latest/AppSuite/ScanningDiffraction</span></a> for details.</p></body></html>"))
        # self.textBrowser_5.setMarkdown(_translate("LauncherForm", "**Diffraction Centroids** is designed to rapidly and accurately measure the\n"
# "spacings of user specified meridional reflections as well as the 5.9 and 5.1\n"
# "actin layer lines in a series of diffraction images, such as those generated in\n"
# "a time resolved experiment. "))
#         self.textBrowser_5.setHtml(_translate("LauncherForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Diffraction Centroids</span> is designed to rapidly and accurately measure the spacings of user specified meridional reflections as well as the 5.9 and 5.1 actin layer lines in a series of diffraction images, such as those generated in a time resolved experiment.<br /><br />See <a href=\"https://musclex.readthedocs.io/en/latest/AppSuite/DiffractionCentroids\"><span style=\" color:#0000ff;\">https://musclex.readthedocs.io/en/latest/AppSuite/DiffractionCentroids</span></a> for details.</p></body></html>"))
        self.textBrowser_6.setMarkdown(_translate("LauncherForm", "**DDF Processor** is a program which is able to average data points for ddf file."))
        self.textBrowser_6.setHtml(_translate("LauncherForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">DDF Processor</span> is a program which is able to average data points for ddf file.<br /><br />See <a href=\"https://musclex.readthedocs.io/en/latest/AppSuite/DDFProcessor\"><span style=\" color:#0000ff;\">https://musclex.readthedocs.io/en/latest/AppSuite/DDFProcessor</span></a> for details.</p></body></html>"))
        self.textBrowser_7.setMarkdown(_translate("LauncherForm", "**Add Intensities Single Experiment** (former Image Merger) is a program which is\n"
"designed to be used with a series of images with sequential file names taken in\n"
"a time resolved experiment. "))
        self.textBrowser_7.setHtml(_translate("LauncherForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Add Intensities Single Experiment</span> (former Image Merger) is a program which is designed to be used with a series of images with sequential file names taken in a time resolved experiment.<br /><br />See <a href=\"https://musclex.readthedocs.io/en/latest/AppSuite/AddIntensitiesSE\"><span style=\" color:#0000ff;\">https://musclex.readthedocs.io/en/latest/AppSuite/AddIntensitiesSE</span></a> for details.</p></body></html>"))
        self.textBrowser_8.setMarkdown(_translate("LauncherForm", "**Add Intensities Multiple Experiments** (former Add Intensities) is a program\n"
"which is designed to be used with a series of images placed across multiple\n"
"folders. It takes the sum of the images in each folder which have the same\n"
"number (For example, F_001.tif in Folder A will map to FP_001.tif in folder B).\n"
"The matched images are then summed together and the resultant sum image is\n"
"stored in `aime_results` folder in the selected directory. "))
        self.textBrowser_8.setHtml(_translate("LauncherForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Add Intensities Multiple Experiments</span> (former Add Intensities) is a program which is designed to be used with a series of images placed across multiple folders. It takes the sum of the images in each folder which have the same number (For example, F_001.tif in Folder A will map to FP_001.tif in folder B). The matched images are then summed together and the resultant sum image is stored in <span style=\" font-family:\'monospace\';\">aime_results</span> folder in the selected directory.<br /><br />See <a href=\"https://musclex.readthedocs.io/en/latest/AppSuite/AddIntensitiesME\"><span style=\" color:#0000ff;\">https://musclex.readthedocs.io/en/latest/AppSuite/AddIntensitiesME</span></a> for details.</p></body></html>"))
        self.quitButton.setText(_translate("LauncherForm", "Quit"))
        self.runButton.setText(_translate("LauncherForm", "Run"))
        self.testButton.setText(_translate("LauncherForm", "Run Tests"))
