from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import sys

class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        loadUi('movie2.ui', self)
        self.show()

app = QApplication(sys.argv)
widget = QStackedWidget()
window = Ui()
widget.addWidget(window)
widget.setFixedHeight(1080)
widget.setFixedWidth(1920)
widget.show()
app.exec_()