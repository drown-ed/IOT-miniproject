from urllib.request import Request, urlopen 
from urllib.parse import quote 
import datetime
import json

class NaverApi:
    def __init__(self) -> None:
        print('Naver API 생성')

    def get_request_url(self, url):
        req = Request(url)
        req.add_header('X-Naver-Client-Id', 'z0rvoy6N_N2K8eHJutiN')
        req.add_header('X-Naver-Client-Secret', 'tlImGqSbZ7')

        try:
            res = urlopen(req)
            if res.getcode() == 200: # response OK
                print(f'[{datetime.datetime.now()}]')
                return res.read().decode('')
            else:
                print(f'[{datetime.datetime.now()}]')
                return None
        except Exception as e:
            print(f'[{datetime.datetime.now()}] 예외 발생 : {e}')
            return None

    def get_naver_search(self, node, search, start, display):
        base_url = 'https://openapi.naver.com/v1/search'
        node_url = f'/{node}.json'
        params = f'?query={search}&start={start}&display={display}'

        url = base_url + node_url + params 
        retData = self.get_request_url(url)

        if retData == None:
            return None 
        else:
            return json.loads(retData)

    def get_post_data(self):
        pass 

