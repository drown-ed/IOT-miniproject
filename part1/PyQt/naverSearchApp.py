# Qt Designer로 디자인
import sys
from importlib import reload
from PyQt5 import uic
from PyQt5.QtWidgets import *
from NaverApi import * 

class qtApp(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('part1/PyQt/NaversearchUI.ui', self)

        # 검색 버튼 클릭 시그널에 대한 슬롯 함수
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        self.textSearch.returnPressed.connect(self.textSearchResturned)

    def textSearchResturned(self):
        self.btnSearchClicked()

    def btnSearchClicked(self):
        search = self.textSearch.text()

        if search == '':
            QMessageBox.warning(self, '경고', '검색어를 입력하세요.')
            return
        else:
            api = NaverApi() # NaverApi 클래스 객체 생성
            node = 'news' # movie로 검색하면 영화검색
            display = 100

            result = api.get_naver_search(node, search, 1, display)
            # print(result)

            while result != None and result['display'] != 0:
                for post in result['items']:
                    api.get_post_data(posts, outputs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())