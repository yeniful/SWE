import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("QMainWindow Event")
        self.setGeometry(300, 300, 300, 400)

        btn1 = QPushButton("Click me", self)# 클래스 QPushButton 에서 객체 btm1 생성
        btn1.move(20, 20) # 좌표
        btn1.clicked.connect(self.btn1_clicked) # 클릭하면 def  btn1_clicked로 연결

    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked")

app = QApplication(sys.argv)
myWindow = MyWindow()
myWindow.show()
app.exec_()
