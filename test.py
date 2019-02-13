# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from random import shuffle
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        json1_file = open('QNA.json')
        json1_str = json1_file.read()
        self.qs = json.loads(json1_str)
        self.quesnim = []
        self.a = []
        for i in self.qs:
            self.quesnim.append(i)
        for i in self.quesnim:
            self.a.append(self.qs[i])
        shuffle(self.quesnim)
        self.ques = []
        self.images = []
        self.x = 0
        for i in self.qs:
            self.ques.append(i.split(":")[0])
            self.images.append(i.split(":")[1])
        for i in range(0, len(self.images)):
            if self.images[i] == " ":
                self.images[i] = "images/noim.jpg"
            else:
                pass
        #TODO make an window for making QnA json files
        #todo load different json files
        #todo make another title window for loading json files + making json files
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 400, 200, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 403, 80, 15))
        self.pushButton.setObjectName("pushButton")

        self.anwsers = QtWidgets.QListWidget(self.centralwidget)
        self.anwsers.setGeometry(QtCore.QRect(170, 480, 200, 200))
        self.anwsers.setObjectName("ListView")
        self.anwsers.addItems(self.a)

        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(70, 60, 520, 320))
        pixmap = QPixmap(self.images[self.x])
        pixmap = pixmap.scaled(self.image.width(), self.image.height())
        self.image.setPixmap(QPixmap(pixmap))
        self.image.setObjectName("label")
        self.q = QtWidgets.QLabel(self.centralwidget)
        self.q.setGeometry(QtCore.QRect(250, 10, 2000, 40))
        self.q.setText(self.ques[self.x])
        self.q.setObjectName("Q")
        self.c = QtWidgets.QLabel(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(170, 420, 460, 40))
        self.c.setText("")
        self.c.setObjectName("C")
        self.e = QtWidgets.QLabel(self.centralwidget)
        self.e.setGeometry(QtCore.QRect(170, 440, 460, 40))
        self.e.setText("")
        self.e.setObjectName("C")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 15))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.on_click)
        self.lineEdit.returnPressed.connect(self.on_click)
        self.image.showMaximized()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dyllan\'s Exam Studier"))
        MainWindow.setWindowIcon(QtGui.QIcon("images/noim.jpg"))
        #change icon here
        self.pushButton.setText(_translate("MainWindow", "Answer"))

    def on_click(self):
        self.q.clear()
        self.q.setText(self.ques[self.x])
        if self.x < len(self.ques)-1:
            anwser = self.lineEdit.text().lower()
            if self.images[self.x] != "images/noim.jpg":
                real = self.ques[self.x] + ":" + self.images[self.x]
            else:
                real = self.ques[self.x] + ": "

            if anwser == self.qs[real].lower():
                self.e.clear()
                self.c.clear()
                self.c.setText("Correct!" + " " + self.ques[self.x] + " " + self.qs[real])
                self.image.clear()
                self.x += 1
                pixmap = QPixmap(self.images[self.x])
                pixmap = pixmap.scaled(self.image.width(), self.image.height())
                self.image.setPixmap(QPixmap(pixmap))
                self.q.clear()
                self.q.setText(self.ques[self.x])
            else:
                self.e.clear()
                self.c.clear()
                self.c.setText("Wrong" + " " + self.ques[self.x] + " " + self.qs[real])
                self.x+=1
                self.image.clear()
                pixmap = QPixmap(self.images[self.x])
                pixmap = pixmap.scaled(self.image.width(), self.image.height())
                self.image.setPixmap(QPixmap(pixmap))
                self.q.clear()
                self.q.setText(self.ques[self.x])
            self.lineEdit.clear()

        else:
            anwser = self.lineEdit.text().lower()
            if self.images[self.x] != "images/noim.jpg":
                real = self.ques[self.x] + ":" + self.images[self.x]
            else:
                real = self.ques[self.x] + ": "
            if anwser == self.qs[real].lower():
                self.e.clear()
                self.c.clear()
                self.c.setText("Correct!" + " " + self.ques[self.x] + " " + self.qs[real])
            else:
                self.e.clear()
                self.c.clear()
                self.c.setText("Wrong" + " " + self.ques[self.x] + " " + self.qs[real])

            self.lineEdit.clear()
            self.e.clear()
            self.e.setText("Out of Questions reshuffling")
            self.x = 0
            shuffle(self.quesnim)
            self.ques = []
            self.images = []
            self.x = 0
            for i in self.qs:
                self.ques.append(i.split(":")[0])
                self.images.append(i.split(":")[1])
            for i in range(0, len(self.images)):
                if self.images[i] == " ":
                    self.images[i] = "images/noim.jpg"
                else:
                    pass
            pixmap = QPixmap(self.images[self.x])
            pixmap = pixmap.scaled(self.image.width(), self.image.height())
            self.image.setPixmap(QPixmap(pixmap))
            self.q.clear()
            self.q.setText(self.ques[self.x])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

