# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(352, 595)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: black; /* Set the background color to black */\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_answer = QtWidgets.QLabel(self.centralwidget)
        self.lbl_answer.setGeometry(QtCore.QRect(10, 10, 330, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_answer.setFont(font)
        self.lbl_answer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_answer.setAutoFillBackground(False)
        self.lbl_answer.setStyleSheet("QLabel {\n"
"    color: white; /* Change \'red\' to your desired color */\n"
"}\n"
"")
        self.lbl_answer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_answer.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_answer.setLineWidth(3)
        self.lbl_answer.setMidLineWidth(0)
        self.lbl_answer.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_answer.setObjectName("lbl_answer")
        self.btn_clr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clr.setGeometry(QtCore.QRect(10, 160, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clr.setFont(font)
        self.btn_clr.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.btn_clr.setAutoFillBackground(False)
        self.btn_clr.setStyleSheet("QPushButton#btn_clr {\n"
"    border-radius: 15px;\n"
"    background-color: #ffd167; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_clr.setObjectName("btn_clr")
        self.lbl_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_answer_2.setGeometry(QtCore.QRect(10, 105, 330, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_answer_2.setFont(font)
        self.lbl_answer_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_answer_2.setAutoFillBackground(False)
        self.lbl_answer_2.setStyleSheet("QLabel {\n"
"    color: white; /* Change \'red\' to your desired color */\n"
"}\n"
"")
        self.lbl_answer_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_answer_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_answer_2.setLineWidth(3)
        self.lbl_answer_2.setMidLineWidth(0)
        self.lbl_answer_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_answer_2.setObjectName("lbl_answer_2")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(95, 160, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_divide.setFont(font)
        self.btn_divide.setAutoFillBackground(False)
        self.btn_divide.setStyleSheet("QPushButton#btn_divide {\n"
"    border-radius: 15px;\n"
"    background-color: #fda481; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_divide.setObjectName("btn_divide")
        self.btn_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.btn_subtract.setGeometry(QtCore.QRect(265, 160, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_subtract.setFont(font)
        self.btn_subtract.setAutoFillBackground(False)
        self.btn_subtract.setStyleSheet("QPushButton#btn_subtract {\n"
"    border-radius: 15px;\n"
"    background-color: #fda481; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_subtract.setObjectName("btn_subtract")
        self.btn_num7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num7.setGeometry(QtCore.QRect(10, 245, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num7.setFont(font)
        self.btn_num7.setAutoFillBackground(False)
        self.btn_num7.setStyleSheet("QPushButton#btn_num7 {\n"
"    border-radius: 15px;\n"
"    background-color: #37415c; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_num7.setObjectName("btn_num7")
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setGeometry(QtCore.QRect(180, 160, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_multiply.setFont(font)
        self.btn_multiply.setAutoFillBackground(False)
        self.btn_multiply.setStyleSheet("QPushButton#btn_multiply {\n"
"    border-radius: 15px;\n"
"    background-color: #fda481; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_num8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num8.setGeometry(QtCore.QRect(95, 245, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num8.setFont(font)
        self.btn_num8.setAutoFillBackground(False)
        self.btn_num8.setStyleSheet("QPushButton#btn_num8 {\n"
"    border-radius: 15px;\n"
"    background-color: #37415c; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_num8.setObjectName("btn_num8")
        self.btn_num9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num9.setGeometry(QtCore.QRect(180, 245, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num9.setFont(font)
        self.btn_num9.setAutoFillBackground(False)
        self.btn_num9.setStyleSheet("QPushButton#btn_num9 {\n"
"    border-radius: 15px;\n"
"    background-color: #37415c; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_num9.setObjectName("btn_num9")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(265, 245, 75, 160))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setAutoFillBackground(False)
        self.btn_add.setStyleSheet("QPushButton#btn_add {\n"
"    border-radius: 15px;\n"
"    background-color: #fda481; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_add.setObjectName("btn_add")
        self.btn_num5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num5.setGeometry(QtCore.QRect(95, 330, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num5.setFont(font)
        self.btn_num5.setAutoFillBackground(False)
        self.btn_num5.setStyleSheet("QPushButton#btn_num5 {\n"
"    border-radius: 15px;\n"
"    background-color: #37415c; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_num5.setObjectName("btn_num5")
        self.btn_num6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num6.setGeometry(QtCore.QRect(180, 330, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num6.setFont(font)
        self.btn_num6.setAutoFillBackground(False)
        self.btn_num6.setStyleSheet("QPushButton#btn_num6 {\n"
"    border-radius: 15px;\n"
"    background-color: #37415c; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_num6.setObjectName("btn_num6")
        self.btn_num4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num4.setGeometry(QtCore.QRect(10, 330, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num4.setFont(font)
        self.btn_num4.setAutoFillBackground(False)
        self.btn_num4.setStyleSheet("QPushButton#btn_num4 {\n"
"    border-radius: 15px;\n"
"    background-color: #37415c; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_num4.setObjectName("btn_num4")
        self.btn_num1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num1.setGeometry(QtCore.QRect(10, 415, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num1.setFont(font)
        self.btn_num1.setAutoFillBackground(False)
        self.btn_num1.setStyleSheet("QPushButton#btn_num1 {\n"
"    border-radius: 15px;\n"
"    background-color: #37415c; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_num1.setObjectName("btn_num1")
        self.btn_num2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num2.setGeometry(QtCore.QRect(95, 415, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num2.setFont(font)
        self.btn_num2.setAutoFillBackground(False)
        self.btn_num2.setStyleSheet("QPushButton#btn_num2 {\n"
"    border-radius: 15px;\n"
"    background-color: #37415c; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_num2.setObjectName("btn_num2")
        self.btn_num3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num3.setGeometry(QtCore.QRect(180, 415, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num3.setFont(font)
        self.btn_num3.setAutoFillBackground(False)
        self.btn_num3.setStyleSheet("QPushButton#btn_num3 {\n"
"    border-radius: 15px;\n"
"    background-color: #37415c; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_num3.setObjectName("btn_num3")
        self.btn_num0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num0.setGeometry(QtCore.QRect(10, 500, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num0.setFont(font)
        self.btn_num0.setAutoFillBackground(False)
        self.btn_num0.setStyleSheet("QPushButton#btn_num0 {\n"
"    border-radius: 15px;\n"
"    background-color: #37415c; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_num0.setObjectName("btn_num0")
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(180, 500, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dot.setFont(font)
        self.btn_dot.setAutoFillBackground(False)
        self.btn_dot.setStyleSheet("QPushButton#btn_dot {\n"
"    border-radius: 15px;\n"
"    background-color: #37415c; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_dot.setObjectName("btn_dot")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(265, 415, 75, 160))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equal.setFont(font)
        self.btn_equal.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.btn_equal.setAutoFillBackground(False)
        self.btn_equal.setStyleSheet("QPushButton#btn_equal {\n"
"    border-radius: 15px;\n"
"    background-color: #ffd167; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_equal.setObjectName("btn_equal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QT Calculator by Kenny Neutron"))
        self.lbl_answer.setText(_translate("MainWindow", "0"))
        self.btn_clr.setText(_translate("MainWindow", "CLR"))
        self.lbl_answer_2.setText(_translate("MainWindow", "0"))
        self.btn_divide.setText(_translate("MainWindow", "/"))
        self.btn_subtract.setText(_translate("MainWindow", "-"))
        self.btn_num7.setText(_translate("MainWindow", "7"))
        self.btn_multiply.setText(_translate("MainWindow", "x"))
        self.btn_num8.setText(_translate("MainWindow", "8"))
        self.btn_num9.setText(_translate("MainWindow", "9"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_num5.setText(_translate("MainWindow", "5"))
        self.btn_num6.setText(_translate("MainWindow", "6"))
        self.btn_num4.setText(_translate("MainWindow", "4"))
        self.btn_num1.setText(_translate("MainWindow", "1"))
        self.btn_num2.setText(_translate("MainWindow", "2"))
        self.btn_num3.setText(_translate("MainWindow", "3"))
        self.btn_num0.setText(_translate("MainWindow", "0"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_equal.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())