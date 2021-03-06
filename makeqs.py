# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(270, 60, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setDisabled(True)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 90, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 140, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(30, 230, 90, 20))
        self.add.setObjectName("add")
        self.add.clicked.connect(self.add_to_list)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 190, 90, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add_image)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 190, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setDisabled(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 151, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 40, 171, 16))
        self.label_4.setObjectName("label_4")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 15))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        #MainWindow.setMenuBar(self.menubar)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.Save_File)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Making Questions"))
        self.add.setText(_translate("MainWindow", "Add Question"))
        self.pushButton_2.setText(_translate("MainWindow", "Open Image"))
        self.label.setText(_translate("MainWindow", "Question"))
        self.label_2.setText(_translate("MainWindow", "Anwser"))
        self.label_3.setText(_translate("MainWindow", "Image If Any"))
        self.label_4.setText(_translate("MainWindow", "Questions"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

    def add_to_list(self):
        image = self.lineEdit_3.text()
        if image == "":
            image = " "
        an = self.lineEdit_2.text()
        question = self.lineEdit.text()
        if "|" in image or "|" in an or "|" in question or "" == an or "" == question:
            reply = QtWidgets.QMessageBox.question(self, "ERROR",
                                           "Re-enter your question either your question or anwser conatained a '|' or was lefted blank",
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Cancel)
            if reply:
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
        else:
            self.listWidget.addItem(question + ":" + image + "|" + an)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()

    def add_image(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QFileDialog(), "QFileDialog.getOpenFileName()",
                                                            "",
                                                            "All Files(*.*)", options=options)
        if fileName:
            self.lineEdit_3.setText(fileName)

    def Save_File(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QFileDialog(), "QFileDialog.getSaveFileName()",
                                                            "",
                                                            "Json Files (*.json)", options=options)
        if fileName:
            data = {}
            for i in range(0, self.listWidget.count()):
                d = self.listWidget.item(i).text()
                d = d.split("|")
                qnim = d[0]
                an = d[1]
                data[qnim] = an
            fileName = fileName + ".json"
            with open(fileName, "w") as file:
                json.dump(data, file)
            file.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

