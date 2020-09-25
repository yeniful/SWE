import sys
from PyQt4 import QtCore, QtGui, uic
form_class=uic.loadUiType("temp.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.C2F.clicked.connect(self.clicked)
        self.F2C.clicked.connect(self.clicked)
        a=[str(self.C2F.text()), str(self.F2C.text())]
        print a

    def clicked(self):
        if self.sender()==self.C2F:
            print "C2F"

    def keyPressEvent(self, event):
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_A :
            print "A"

app=QtGui.QApplication(sys.argv)
myWindow=MyWindowClass(None)
myWindow.show()
app.exec_()


