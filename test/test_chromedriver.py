## 사전작업
# pip install selenium
# pip freeze > requirements.txt
import time

from selenium import webdriver

wd = webdriver.Chrome('C:\\KDigital-AI\\chromedriver_win32\\chromedriver.exe')
wd.get('https://www.google.com')

time.sleep(3) # 웹이 실행되고 3초 뒤에 꺼짐 (3초 동안 실행됨)
html = wd.page_source
print(html)

wd.close()