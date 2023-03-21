import sys
import pymysql
from datetime import datetime

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class qtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('오유리나\weather.ui',self)

        self.initDB() #DB 초기화

        
    def initDB(self):
        self.conn=pymysql.connect(host='210.119.12.66', user = 'root', password='12345',
                                db = 'miniproject01', charset='utf8')
        cur=self.conn.cursor() #커서
        query='''
        SELECT log_date, log_time
            , pop, pty, pcp, reh, sno, sky, tmp, tmn, tmx, uuu, vvv, wav, vec, wsd
        FROM ohyurina ORDER BY log_date
        '''
        cur.execute(query)
        rows=cur.fetchall() 
        newrow = []

        for i in range(0, len(rows)):
            if int(rows[i][0]) == int(datetime.today().strftime("%Y%m%d")):
                if int(rows[i][1][:2]) >= int(datetime.now().hour):
                    newrow.append(rows[i])
            elif int(rows[i][0]) > int(datetime.today().strftime("%Y%m%d")):
                newrow.append(rows[i])

        self.todayweather(newrow)
        self.makeTable(newrow)
        self.conn.close() #프로그램 종료


    def todayweather(self, newrow):
        self.todaytxt.setText(f'{datetime.today().strftime("%Y")}년 {datetime.today().strftime("%m")}월 {datetime.today().strftime("%d")}일 {datetime.now().hour}시')
        
        self.qPixmapVar = QPixmap()

        PATH = '오유리나/image/'

        if newrow[0][3] == 0:                         # sunny
            if newrow[0][7] == 1: 
                self.qPixmapVar.load(f'{PATH}day_clear.png')
            else:
                self.qPixmapVar.load(f'{PATH}cloudy.png')
        elif newrow[0][3] == 3:                       # snow
            self.qPixmapVar.load(f'{PATH}snow.png')
        else:                                           # rain
            self.qPixmapVar.load(f'{PATH}rain.png')

        self.qPixmapVar = self.qPixmapVar.scaledToWidth(110)
        self.todayimg.setPixmap(self.qPixmapVar)
        
        conn=pymysql.connect(host='210.119.12.66', user = 'root', password='12345',
                        db = 'miniproject01', charset='utf8')
        cur=conn.cursor() #커서
        query=f'SELECT max(tmx) FROM ohyurina WHERE log_date ={datetime.today().strftime("%Y%m%d")}'
        cur.execute(query)
        hightm = cur.fetchall() 

        query=f'SELECT max(tmn) FROM ohyurina WHERE log_date ={datetime.today().strftime("%Y%m%d")}'
        cur.execute(query)
        lowtm = cur.fetchall() 
        

        self.hightmp.setText(f'{hightm[0][0]}°C')
        self.lowtmp.setText(f'{lowtm[0][0]}°C')

        self.nowtmp.setText(f'{newrow[0][8]}°')
        self.nowreh.setText(f'{newrow[0][5]}%')
        self.nowpop.setText(f'{newrow[0][3]}%')
        

    #Qt Designer에서 만든 ui에 db에 저장된 정보 뿌려주기
    def makeTable(self,rows):
        self.tblAddress.setColumnCount(16)#열갯수
        self.tblAddress.setRowCount(len(rows))#행갯수
        self.tblAddress.setSelectionMode(QAbstractItemView.SingleSelection)#단일선택
        self.tblAddress.setHorizontalHeaderLabels(['날짜','시간', '강수확률', '강수형태', '1시간 강수량','습도','1시간 신적설',
                                                '하늘상태', '1시간 기온', '일 최저기온', '일 최고기온', '풍속(동서)', '풍속(남북)', '파고', '풍향', '풍속'])
        # self.tblAddress.setColumnWidth(0,10) # 번호는 숨김
        # self.tblAddress.setColumnWidth(1,70) # 이름 열 사이즈 70
        # self.tblAddress.setColumnWidth(2,105) # 핸드폰 열 사이즈 105
        # self.tblAddress.setColumnWidth(3,175) # 이메일 열 사이즈 175
        # self.tblAddress.setColumnWidth(4,200) # 주소 열 사이즈 200
        self.tblAddress.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼 수정 금지
        

        for i,row in enumerate(rows):
            for j in range(0, len(row)): 
                self.tblAddress.setItem(i, j, QTableWidgetItem(str(row[j])))


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=qtApp()
    ex.show()
    sys.exit(app.exec_())
