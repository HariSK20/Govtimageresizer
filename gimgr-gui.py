# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PIL import Image, ImageDraw
from PyQt5.QtGui import QIntValidator

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.onlyInt = QIntValidator()
        self.isImage = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 538)
        MainWindow.setMinimumSize(QtCore.QSize(464, 538))
        MainWindow.setMaximumSize(QtCore.QSize(464, 538))
        font = QtGui.QFont()
        font.setItalic(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Main = QtWidgets.QLabel(self.centralwidget)
        self.label_Main.setGeometry(QtCore.QRect(0, 0, 471, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(51, 106, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 106, 188, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 106, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 106, 188, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 174, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 47, 52, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_Main.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(36)
        font.setItalic(False)
        self.label_Main.setFont(font)
        self.label_Main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Main.setObjectName("label_Main")
        self.label_link = QtWidgets.QLabel(self.centralwidget)
        self.label_link.setGeometry(QtCore.QRect(130, 480, 191, 18))
        self.label_link.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_link.setAlignment(QtCore.Qt.AlignCenter)
        self.label_link.setOpenExternalLinks(True)
        self.label_link.setObjectName("label_link")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 140, 241, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.input_Height = QtWidgets.QLineEdit(self.frame)
        self.input_Height.setText("")
        self.input_Height.setMaxLength(4)
        self.input_Height.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_Height.setObjectName("input_Height")
        self.input_Height.setValidator(self.onlyInt)
        self.input_Width = QtWidgets.QLineEdit(self.frame)
        self.input_Width.setValidator(self.onlyInt)
        self.input_Width.setMaxLength(4)
        self.input_Width.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_Width.setObjectName("input_Width")
        self.gridLayout.addWidget(self.input_Height, 0, 1, 1, 1)
        self.label_Width_px = QtWidgets.QLabel(self.frame)
        self.label_Width_px.setObjectName("label_Width_px")
        self.gridLayout.addWidget(self.label_Width_px, 1, 3, 1, 1)
        self.label_px_Height = QtWidgets.QLabel(self.frame)
        self.label_px_Height.setObjectName("label_px_Height")
        self.gridLayout.addWidget(self.label_px_Height, 0, 3, 1, 1)
        self.label_Height = QtWidgets.QLabel(self.frame)
        self.label_Height.setObjectName("label_Height")
        self.gridLayout.addWidget(self.label_Height, 0, 0, 1, 1)
        self.label_Size = QtWidgets.QLabel(self.frame)
        self.label_Size.setObjectName("label_Size")
        self.gridLayout.addWidget(self.label_Size, 2, 0, 1, 1)
        self.input_Size = QtWidgets.QLineEdit(self.frame)
        self.input_Size.setMaxLength(5)
        self.input_Size.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_Size.setObjectName("input_Size")
        self.input_Size.setValidator(self.onlyInt)
        self.gridLayout.addWidget(self.input_Size, 2, 1, 1, 1)
        self.label_Width = QtWidgets.QLabel(self.frame)
        self.label_Width.setObjectName("label_Width")
        self.gridLayout.addWidget(self.label_Width, 1, 0, 1, 1)
        self.label_Kb = QtWidgets.QLabel(self.frame)
        self.label_Kb.setObjectName("label_Kb")
        self.gridLayout.addWidget(self.label_Kb, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.input_Width, 1, 1, 1, 1)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 310, 230, 88))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_Name = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_Name.setObjectName("checkBox_Name")
        self.gridLayout_2.addWidget(self.checkBox_Name, 0, 0, 1, 1)


        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 1, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 1, 1, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(260, 140, 181, 261))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_Image = QtWidgets.QLabel(self.frame_3)
        self.label_Image.setGeometry(QtCore.QRect(20, 10, 151, 191))
        self.label_Image.setText("")
        self.label_Image.setPixmap(QtGui.QPixmap(":/Photo/avatar.jpg"))
        self.label_Image.setScaledContents(True)
        self.label_Image.setObjectName("label_Image")
        self.layoutWidget = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 210, 105, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.button_ChangePhoto = QtWidgets.QPushButton(self.layoutWidget)
        self.button_ChangePhoto.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.button_ChangePhoto.setObjectName("button_ChangePhoto")
        self.gridLayout_3.addWidget(self.button_ChangePhoto, 0, 0, 1, 1)
        self.button_Download = QtWidgets.QPushButton(self.centralwidget)
        self.button_Download.setGeometry(QtCore.QRect(300, 420, 103, 34))
        self.button_Download.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_Download.setAutoDefault(True)
        self.button_Download.setDefault(True)
        self.button_Download.setFlat(False)
        self.button_Download.setObjectName("button_Download")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 410, 231, 51))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 201, 34))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.button_ChangePhoto.clicked.connect(self.ChangeImage)
        self.button_Download.clicked.connect(self.handler_Download)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Main.setText(_translate("MainWindow", "Photo Resizer"))
        self.label_link.setText(_translate("MainWindow", "www.sarkarjoli.com"))
        self.label_Width_px.setText(_translate("MainWindow", "px"))
        self.label_px_Height.setText(_translate("MainWindow", "px"))
        self.label_Height.setText(_translate("MainWindow", "Height"))
        self.label_Size.setText(_translate("MainWindow", "Size"))
        self.label_Width.setText(_translate("MainWindow", "Width"))
        self.label_Kb.setText(_translate("MainWindow", "Kb"))
        self.checkBox_Name.setText(_translate("MainWindow", "Name"))
        self.checkBox.setText(_translate("MainWindow", "Date"))
        self.button_ChangePhoto.setText(_translate("MainWindow", "Upload Photo"))
        self.button_Download.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "Format"))
        self.comboBox.setItemText(0, _translate("MainWindow", "jpeg"))
        self.comboBox.setItemText(1, _translate("MainWindow", "gif"))
        self.comboBox.setItemText(2, _translate("MainWindow", "pdf"))
        self.label_2.setText(_translate("MainWindow", "Photo reizer is a free program which helps you to resize the width, length, format and size of any image acccording to the specifications provided by various government agencies"))

    def CalculateImageRatio(self):  
        img_width, img_height = self.img.width, self.img.height
        ratio = img_width/img_height
        input_ratio = self.max_width/self.max_height
        print(ratio)
        if ratio > input_ratio:
            img_width = self.max_width
            img_height = int(img_width/ratio) 
        else:
            img_height = self.max_height
            img_width = int(img_height*ratio)
        self.width, self.height = img_width, img_height

        # if img_width > img_height:
            # img_width = self.max_width
            # img_height = int(img_width/ratio) 
        # else:
            # img_height = self.max_height
            # img_width = int(img_height*ratio)
        # self.width, self.height = img_width, img_height
        print(self.width, self.height)

    def check_Input(self):
        self.max_width = self.input_Width.text()
        self.max_height = self.input_Height.text()
        self.max_size = self.input_Size.text()
        print(self.max_width, self.max_height, self.max_size, self.isImage)
        for ele in self.max_width, self.max_height, self.max_size, self.isImage:
            if not ele:
                return 0
        self.max_width = int(self.input_Width.text())
        self.max_height = int(self.input_Height.text())
        self.max_size = int(self.input_Size.text())
        return 1

    def handler_Download(self):
        if not self.check_Input():
            self.ShowError("Please enter the required information")
        else:
            print("Calculating Image Dimensions")
            #self.CalculateImage()
            self.SaveImage()

    def ShowError(self, string):
        err = QMessageBox()
        err.setWindowTitle("Input Error !")
        err.setText(string)
        err.setIcon(QMessageBox.Warning)
        x = err.exec_()
    
#added by HariSK20    
    def add_date(self, margin = 0):
        from PIL import ImageDraw, ImageFont
        img_width, img_height = self.img.width + 2*margin, int( 1.2* self.img.height) + 3*margin
#        fnt_size = int( 0.8*self.img.width/100)
        fnt = ImageFont.load_default()
        img_width, img_height = self.img.width + 2*margin, int( 1.1* self.img.height) + 3*margin
        blank_img = Image.new("RGB",(img_width, img_height), color = "white")
        img2 = self.img
        tmp_date = self.dateEdit.date() 
        date = str(tmp_date.toPyDate())
        dte = ""
        cnt = 1
        print(date.split('-'))
        for i in date.split('-')[::-1]:
            dte = dte + i
            cnt +=1
            if cnt<=3:
                dte = dte + "-"
        blank_img.paste(img2,( margin, margin))
        d = ImageDraw.Draw(blank_img)
        fnt_width, fnt_height = fnt.getsize(date)
        d.text(((self.img.width//2 - fnt_width//2), int(img_height/4 + 0.75*self.img.height)), dte, fill = (100,100,100))
        self.img = blank_img

    def ChangeImage(self):
        self.filepath = QFileDialog.getOpenFileName()
        self.label_Image.setPixmap(QtGui.QPixmap(self.filepath[0]))
        self.button_ChangePhoto.setText("Change Photo")
        self.isImage = 1
        self.img = Image.open(self.filepath[0])
        print(self.img.width, self.img.height)

    def SaveImage(self):
        if self.checkBox.isChecked():
            self.add_date()
        self.format = str(self.comboBox.currentText())
        if self.format == "jpeg":
            self.img = self.img.resize((self.max_width,self.max_height), Image.ANTIALIAS)
        if self.format == "pdf":
            self.img = self.img.convert('RGB')
        name = QFileDialog.getSaveFileName()
        name = name[0] + "." + self.format
        if '.' in name:
            if name.split('.')[1] != self.format:
                self.ShowError("Format Error")
        print(name)
        self.img.save(name)


import resource_rc



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
