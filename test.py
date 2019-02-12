# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from random import shuffle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.qs = {"Number of Triple Points: ":"N", "Number of Phases: ":"PI", "Delta U : ":"cvDt",
                   "Detla W: ":" -int(pdv)", "Mass Balance: ":"UA/V2+UA/V3-UA/V1=0", "Delta H: ":"cpDt"}
        self.ques = []
        self.images = []
        self.x = 0
        for i in self.qs:
            self.ques.append(i.split(":")[0])
            self.images.append(i.split(":")[1])
        #TODO add quw=estions to list then shuffle list then split up images and ques
        #TODO add another label on bottom for reshuffle notification, add list of anwsers
        #TODO add first todo code for reshuffle to work, also twick reshuffling to work proparly
        #TODO change window image and title
        #TODO add a no image for questions without images
        shuffle(self.ques)
        MainWindow.setObjectName("Dyllan")
        MainWindow.setWindowTitle("Dyllan's Exam Studier")
        MainWindow.resize(798, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 220, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 220, 80, 15))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 40, 221, 151))
        pixmap = QPixmap(self.images[0])
        self.label.setPixmap(QPixmap(pixmap))
        self.label.setObjectName("label")
        self.q = QtWidgets.QLabel(self.centralwidget)
        self.q.setGeometry(QtCore.QRect(270, 0, 2000, 40))
        self.q.setText(self.ques[self.x])
        self.q.setObjectName("Q")
        self.c = QtWidgets.QLabel(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(270, 240, 460, 40))
        self.c.setText("")
        self.c.setObjectName("C")
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dyllan\'s Exam Studier"))
        self.pushButton.setText(_translate("MainWindow", "Answer"))

    def on_click(self):
        self.label.clear()
        pixmap = QPixmap(self.images[self.x])
        self.label.setPixmap(pixmap)
        self.q.clear()
        self.q.setText(self.ques[self.x])
        if self.x < len(self.ques)-1:
            anwser = self.lineEdit.text().lower()
            real = self.ques[self.x] + ":" + self.images[self.x]

            if anwser == self.qs[real].lower():
                self.c.clear()
                self.c.setText("Correct!" + " " + self.ques[self.x] + " " + self.qs[real])
                self.label.clear()
                pixmap = QPixmap(self.images[self.x])
                self.label.setPixmap(pixmap)
                self.x+=1
                self.q.clear()
                self.q.setText(self.ques[self.x])
            else:
                self.c.clear()
                self.c.setText("Wrong" + " " + self.ques[self.x] + " " + self.qs[real])
                self.x+=1
                self.q.clear()
                self.q.setText(self.ques[self.x])
            self.lineEdit.clear()
        else:
            self.c.clear()
            self.c.setText("Out of Questions reshuffling")
            self.x = 0
            shuffle(self.ques)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

