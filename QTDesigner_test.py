# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test_QTdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 932)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_ClickMe = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ClickMe.setGeometry(QtCore.QRect(470, 390, 231, 141))
        self.btn_ClickMe.setObjectName("btn_ClickMe")
        self.lbl_MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.lbl_MainLabel.setGeometry(QtCore.QRect(430, 270, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lbl_MainLabel.setFont(font)
        self.lbl_MainLabel.setObjectName("lbl_MainLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_ClickMe.setText(_translate("MainWindow", "Click Me!"))
        self.lbl_MainLabel.setText(_translate("MainWindow", "Hello this is Qt Designer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())