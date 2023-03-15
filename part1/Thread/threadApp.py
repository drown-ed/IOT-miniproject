import sys 
from PyQt5 import uic, QtCore, QtGui 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class BackgroundWorker(QThread):
    procChanged = pyqtSignal(str)
    
    def __init__(self, count = 0, parent = None) -> None:
        super().__init__()
        self.parent = parent
        self.working = True
        self.count = count
    
    def run(self):
        self.parent.pgdTask.setRange(0, 100)
        for i in range(0, 101):
            print(f'스래드 출력 > {i}')
            self.parent.pgdTask.setValue(i)
            self.parent.txtbLog.append(f'thread print > {i}')

        while self.working:
            self.procChanged.emit(f'스레드 출력 > {self.count}')
            self.count += 1

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('part1/Thread/threadApp.ui', self)
        self.setWindowTitle('No Thread App')
        self.pgdTask.setValue(0)

        self.btnStart.clicked.connect(self.btnStartClicked)

        self.worker = BackgroundWorker(parent= self)
        self.worker.procChanged.connect(self.procUpdated)

    def btnStartClicked(self):
        th = BackgroundWorker(self)
        th.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex=qtApp()
    ex.show()
    sys.exit(app.exec_())