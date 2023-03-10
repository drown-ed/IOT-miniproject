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

        self.initDB()

    def initDB(self):
        self.conn = pymysql.connect(host = 'localhost', user = 'root', password = '1234',
                                    db = 'miniproject', charset = 'utf8')
        cur = self.conn.cursor()
        query = ''' SELECT Idx,
                           FullName,
                           PhoneNumber,
                           Email,
                           Address
                     FROM addressbook
            '''
        cur.execute(query)
        rows = cur.fetchall()

        print(rows)
        self.makeTable(rows)
        self.conn.close()

    def makeTable(self, rows):
        self.tblAdd.setColumnCount(5)
        self.tblAdd.setRowCount(len(rows))
        self.tblAdd.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblAdd.setHorizontalHeaderLabels(['번호', '이름', '핸드폰', '이메일', '주소'])
        self.tblAdd.setColumnWidth(0, 0)
        self.tblAdd.setColumnWidth(1, 70)
        self.tblAdd.setColumnWidth(2, 105)
        self.tblAdd.setColumnWidth(3, 175)
        self.tblAdd.setColumnWidth(4, 200)
        self.tblAdd.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for i, row in enumerate(rows):
            idx = row[0]
            fullName = row[1]
            phoneNum = row[2]
            email = row[3]
            address = row[4]

            self.tblAdd.setItem(i, 0, QTableWidgetItem(idx))
            self.tblAdd.setItem(i, 1, QTableWidgetItem(fullName))
            self.tblAdd.setItem(i, 2, QTableWidgetItem(phoneNum))
            self.tblAdd.setItem(i, 3, QTableWidgetItem(email))
            self.tblAdd.setItem(i, 4, QTableWidgetItem(address))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())