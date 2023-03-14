import sys 
from PyQt5 import uic, QtCore, QtGui 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class BackgroundWorker(QThread):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent= parent
    
    def run(self):
        self.parent.pgdTask.setRange(0, 100)
        for i in range(0, 101):
            print(f'스래드 출력 > {i}')
            self.parent.pgdTask.setValue(i)
            self.parent.txtbLog.append(f'thread print > {i}')

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('part1/Thread/threadApp.ui', self)
        self.setWindowTitle('No Thread App')
        self.pgdTask.setValue(0)

        self.btnStart.clicked.connect(self.btnStartClicked)

    def btnStartClicked(self):
        th = BackgroundWorker(self)
        th.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex=qtApp()
    ex.show()
    sys.exit(app.exec_())