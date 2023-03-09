import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql

class qtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('part1/PyQt/addressbook/personal.ui', self)
        self.setWindowIcon(QIcon('part1/PyQt/addressbook/address.png'))

    def initDB(self):
        self.conn = pymysql.connect(host = 'localhost', user = 'root', password = '1234',
                                    db = 'miniproject', charset = 'utf8')
        cur = self.conn.cursor()
        query = 'SELECT * FROM addressbook'
        cur.execute(query)
        rows = cur.fetchall()

        print(rows)
        self.conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())