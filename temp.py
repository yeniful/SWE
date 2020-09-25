import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUiType

form_class = loadUiType("myfirst.ui")[0]

class MyWindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.C2F.clicked.connect(self.C2F_clicked)
        self.F2C.clicked.connect(self.F2C_clicked)

    def C2F_clicked(self):
        cel = float(self.inputValue.toPlainText()) # 문자를 실수로 바꿔서 cel에 저장
        fahr = cel * 9 / 5.0 + 32 # 섭씨를 화씨로 바꾸는 공식
        self.outputValue.setText(str(fahr)) # 실수인 결과값을 스트링을 바꿔서 저장

    def F2C_clicked(self):
        fahr = float(self.outputValue.toPlainText())
        cel = (fahr - 32) / 9.0 * 5
        self.inputValue.setText(str(cel))
        
app = QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()


