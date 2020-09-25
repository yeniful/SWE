import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow): # PyQt에서 만들어 놓은 QMW 클래스 상속받아서 클래스 생
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("QMainWindow")
        self.setGeometry(300, 300, 300, 400)

app = QApplication(sys.argv)
myWindow = MyWindow() # 만들어놓은 클래스에서 myWindow 객체 생성
myWindow.show()
app.exec_()

# 클래스 이름은 일반적으로 대문자