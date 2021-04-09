# 서버에 연결하는 파일
from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')

conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason) # status: 숫자, reason : 코드 설명

# 성공
# GET / HTTP/1.1 (서버) (url에 www.example.com)
# 200 OK (결과)
if resp.status == 200:
    body = resp.read()
    print(type(body), body)

# 실패 결과
# GET / hello.html HTTP/1.1 (서버) (url에 www.example.com/hello.html)
# 404 Not Found (결과)
conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason)