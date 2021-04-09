from itertools import count
from bs4 import BeautifulSoup
import pandas as pd # pandas는 이렇게 import함
from collection import crawler


def crawling_pelicana():
    results = [] # 데이터 담기

    # 데이터 조회
    # for index in range(110, 200): # 테스트하기 위함
    for index in count(start=1, step=1):
        url = f'https://pelicana.co.kr/store/stroe_search.html?page={index}&branch_name=&gu=&si='
        html = crawler.crawling(url)

        # 파싱
        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': ['table', 'mt20']})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출 (마지막 페이지)
        if (len(tags_tr)) == 0: # 페이지 소스보기를 하면, tbody에 아무것도 없을 때 마지막페이지임 그래서 길이가 0일 때 끝!
            print("끝!" + str(index)) # 마지막 페이지가 어디인지 알 수 있게 str(index) 추가.
            break

        for tag_tr in tags_tr:
            datas = list(tag_tr.strings)
            name = datas[1] # 출력된 결과에서 2번째가 이름이니까 인덱스로 1 (인덱스는 0, 1 이니까)
            address = datas[3] # 출력된 결과에서 4번째에 있으니까 인덱스로 3 (인덱스는 0, 1, 2, 3 이니까)
            sidogugun = address.split()[:2] # split()에서 괄호 안에 아무것도 안하면 알아서 ' '로 구분 해줌
            # print(sidogugun)
            # print(name, address, sidogu)

            t = (name, address) + tuple(sidogugun)
            results.append(t)

    # print(results)

    # store (pandas: table로 만들어주는 것) -> pip install pandas 해서 pandas 설치해줘야 가능함.
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'sidogugun'])
    table.to_csv('results/pelicana.csv', encoding='utf-8', mode='w', index=True) # index는 no를 의미함
    # 이렇게 하면 results디렉토리 밑에 pelicana.csv 파일이 생성됨.
    # table에서 입력한 함수의 결과가 그 파일 안에 쓰여있음





def crawling_nene():
    pass


def crawling_kyochon():
    pass






def crawling_goobne():
    pass





if __name__ == '__main__':
    # crawling_pelicana()
    # crawling_nene()
    # crawling_kyochon()
    crawling_goobne()