import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('C:\Source\IOT-miniproject\part1\PyQt\mainApp.ui', self)

        #Qt Designer에서 구성한 위젯 시그널 제작
        
        self.btnOK.clicked.connect(self.btnOKClicked)
        self.btnPOP.clicked.connect(self.btnPOPClicked)
        

    def btnPOPClicked(self):
        QMessageBox.about(self, 'popup', '까꿍')

    # slot func
    def btnOKClicked(self):

        self.lblMessage.clear()
        self.lblMessage.setText('Will you be mine?')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())