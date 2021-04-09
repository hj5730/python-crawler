import sys
from datetime import datetime
from urllib.request import Request, urlopen


def error(e): # crawling 함수의 except 부분에 해당함. (에러니까)
    print(e)
    # print(f'{e}: {datetime.now()}', file=sys.stderr) # 화면으로 나감. stderr은 콘솔을 의미하고 빨간색으로 표시됨

def crawling(url='',
             encoding='utf-8',
             err=error): # crawling 함수의 default 값

    # def error(e)를 다 지워버리고 밑에처럼 err부분만 수정시키면 훨씬 간단해짐
    # err=lambda e: print(f'{e}: {datetime.now()}', file=sys.stderr)):

    try:
        request = Request(url)
        response = urlopen(request)
        print(f'{datetime.now()}: success for request[{url}]') # 성공하면 현재 시간이 출력되면서 저 문구와 url 출력됨

        receive = response.read()
        return receive.decode(encoding, errors='replace')
        # replace 하면 알아서 알맞게 에러 처리를 해줌. 이 에러는 위의 에러와는 다르고 디코딩할때의 에러를 의미함

    except Exception as e:
        if err is not None:
            err(e)
