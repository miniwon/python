"""
인스타그램 로그인 페이지를 실행하기
    크롬에서 인스타그램 로그인 페이지를 개발자모드에서 확인하여
    로그인 폼의 아이디와 비밀번호 입력 name 확인
    아이디 : id
    비밀번호 : pw
"""

from selenium import webdriver

# 0. 인스타그램 로그인 정보
usr='cola_stop_please'
psd='6340040a!'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)   # 3초 대기

# driver.get('http://www.facebook.com')
# driver.get('http://www.daum.net')
# driver.get('http://www.naver.com')
driver.get('http://www.instagram.com')


username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

username.send_keys(usr)
password.send_keys(psd)

btn = driver.find_element_by_css_selector("#loginForm ._ab8w ._acan")
btn.submit()
driver.implicitly_wait(2)