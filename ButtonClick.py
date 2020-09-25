import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("QMainWindow Event")
        self.setGeometry(300, 300, 300, 400)

        b1 = QPushButton(self)
        b1.setText("Button1")
        b1.move(50, 20)
        b1.clicked.connect(self.b1_clicked)

        b2 = QPushButton(self)
        b2.setText("Button2")
        b2.move(50, 50)
        b2.clicked.connect(self.b2_clicked)

    def b1_clicked(self):
        print("Button 1 clicked")
    def b2_clicked(self):
        print("Button 2 clicked")


app = QApplication(sys.argv)
myWindow = MyWindow()
myWindow.show()
app.exec_()