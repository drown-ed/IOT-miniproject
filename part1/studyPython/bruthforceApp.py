# 암호해제 프로그램 

import time 
import itertools
import zipfile 

passwd_string = '0123456789'
#passwd_string = '0123456789abcde'

isFind = False

file = zipfile.ZipFile('part1\studyPython\암호는.zip')

for i in range(1, 5):
    attempts = itertools.product(passwd_string, repeat= i)
    for attempt in attempts:
        try_pass = ''.join(attempt)
        try:
            file.extractall(pwd=try_pass.encode(encoding='utf-8'))
            print(f'암호는 {try_pass}입니다.')
            isFine = True 
            break
        except:
            pass

    if isFind == True: break
        #time.sleep(0.3)
