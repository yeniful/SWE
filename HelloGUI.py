import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World ~~~!")
    w.setGeometry(100, 100, 200, 50)
    b.move(50, 20)
    w.setWindowTitle("pyQt")
    w.show()
    sys.exit(app.exec_())

window()
