from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow #QMainWindow is similar to QWidget(s)
import sys

def clicked_button1():
    print("Button 1 clicked")
    

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 500, 500)  #xpos, ypos, width, height (xpos and ypos are coordinates on your screen)
    win.setWindowTitle("My First App")

    label = QtWidgets.QLabel(win)
    label.setText("Hello World")
    label.move(100, 100)

    btn_Button1 = QtWidgets.QPushButton(win)
    btn_Button1.setText("Button 1")
    btn_Button1.move(200, 200)
    btn_Button1.clicked.connect(clicked_button1)

    win.show()
    sys.exit(app.exec_())

window()