import threading
import time 

class BackgroundWoker(threading.Thread):
    def __init__(self, names: str) -> None:
        super().__init__()
        self._name = f'{threading.current_thread().getName()} : {names}'

    def run(self) -> None:
        print(f'BackgroundWorker start: {self._name}')
        time.sleep(2)
        print(f'BackgroundWorker end : {self._name}')

if __name__ == '__main__':
    print('main thread start')

    for i in range(5):
        name = f'serve thread {i}'
        th = BackgroundWoker(name)
        th.start()
    
    print('main thread end')