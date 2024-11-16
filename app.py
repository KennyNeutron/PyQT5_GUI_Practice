from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow #QMainWindow is similar to QWidget(s)
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 500, 500)  #xpos, ypos, width, height (xpos and ypos are coordinates on your screen)
    win.setWindowTitle("My First App")

    label = QtWidgets.QLabel(win)
    label.setText("Hello World")
    label.move(100, 100)

    win.show()
    sys.exit(app.exec_())

window()