from bs4 import BeautifulSoup

html = '''
<td class="title black">
    <div class="tit3" data-no="10">
        <a href="/movie/bi/mi/basic.nhn?code=189075" title="자산어보">자산어보</a>
    </div>
</td>'''

# 기본 설정. pip install bs4 해야함

# 1. teg 조회하기
def ex01():
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)

    tag_td = bs.td # bs에서 td를 가지고 오기
    # print(tag_td)

    # tag_a = bs.a
    tag_a = tag_td.a # (위에거랑 똑같은데 속도 차이)
    print(tag_a) # string이 아니라 객체임. a만 샥 가져옴

    # None
    tag_h1 = bs.td.h1
    print(tag_h1)


# 2. attribute로 조회 (class)
def ex02():
    bs = BeautifulSoup(html, 'html.parser')

    tag_td = bs.find('td', attrs={'class': ['title', 'black']}) # td를 가지고 오는데, class가 title인 td만 가져옴
    print(tag_td)

    tag_div = bs.find('div', attrs={'class': 'tit3', 'data-no': '10'}) # 딕셔너리로
    print(tag_div)


if __name__ == '__main__': # 실행코드
    # ex01()
    ex02()
