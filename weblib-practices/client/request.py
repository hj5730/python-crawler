from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET
http_response = urlopen('https://www.example.com')
body = http_response.read() # 엔코딩 (한글인데 알아볼수 없는 문구들 \x84 ... 이렇게 쓰여있는 것)
body = body.decode('utf-8') # 디코딩 (그 이상한 암호같은 영어들을 한글로 보여줌(우리가 네이버 화면에서 보는 것처럼))

print(body)

print("=============================================================================")

# POST
data = {
    'id': 'hj5730',
    'name': '김현지',
    'pw': '1234'
}

data = urlencode(data).encode('utf-8') # 한글이 있든 없든 encode('utf-8') 쓰기

request = Request('https://www.example.com', data)
request.add_header('Content-Type', 'text/html')

http_response = urlopen(request) # POST 방식에서는 request 꼭 넣어줘야 함
print(http_response.status, http_response.reason)

body = http_response.read()
html = body.decode('utf-8')

print(html)