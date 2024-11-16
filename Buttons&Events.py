from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow #QMainWindow is similar to QWidget(s)
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 500, 500)  #xpos, ypos, width, height (xpos and ypos are coordinates on your screen)
        self.setWindowTitle("My First App")
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")
        self.label.move(100, 100)

        self.btn_Button1 = QtWidgets.QPushButton(self)
        self.btn_Button1.setText("Button 1")
        self.btn_Button1.move(200, 200)
        self.btn_Button1.clicked.connect(self.clicked_button1)
    
    def clicked_button1(self):
        self.label.setText("Button 1 clicked 01234567890")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()