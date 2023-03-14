import sys 
from PyQt5 import uic, QtCore, QtGui 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('part1/Thread/threadApp.ui', self)
        self.setWindowTitle('No Thread App')
        self.pgdTask.setValue(0)

        self.btnStart.clicked.connect(self.btnStartClicked)

    def btnStartClicked(self):
        
        self.pgdTask.setRange(0, 999999)
        for i in range(0, 1000000):
            print(f'no thread print > {i}')
            self.pgdTask.setValue(i)
            self.txbLog.append(f'no thread print > {i}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex=qtApp()
    ex.show()
    sys.exit(app.exec_())