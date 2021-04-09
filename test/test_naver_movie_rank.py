from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from collection import crawler


def ex01(): # GET 방식
    # 데이터 전체 읽어오기 (조회)
    request = Request("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
    response = urlopen(request)
    html = response.read().decode('cp949')
    # print(html)

    # 파싱 (원하는 것만 꺼내오기)
    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'}) # 한 개가 아니라 여러개니까 find가 아니라 findall
    # print(len(divs)) # class가 tit3 값을 가지는 div의 개수

    # for div in divs:
    #     print(div.a.text) # 태그 div에서 태그 a에 있는 text(문자)만 출력. (태그 출력X)

    for index, div in enumerate(divs):
        print(index+1, div.a.text, div.a['href'], sep=':') # 인덱스가 0부터 나오니까 1부터 나오도록 +1을 함


def ex02(): # ex01을 함수로 만들기
    html = crawler.crawling(
        url='https://movie.naver.com/movie/sdb/rank/rmovie.nhn',
        encoding='cp949') # 원래 3번째 인자는 error인데 인자를 쓰지 않음으로써 디폴트 값 적용
    print(html)

    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})

    for index, div in enumerate(divs):
        print(index+1, div.a.text, div.a['href'], sep=':')


if __name__ == '__main__':
    # ex01()
    ex02()
