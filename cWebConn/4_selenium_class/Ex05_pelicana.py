from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)

# [연습]

for page_no in range(1, 11):
    driver.get('https://pelicana.co.kr/store/stroe_search.html?page=%d' %page_no )
    html = driver.page_source
    # print(html)
    time.sleep(5)

    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.select('table tbody tr')

    print('-' * 20)
    print('매장명 - 전화번호')
    print('-' * 20)

    # 매장명 - 전화번호
    for data in datas:
        dLi = data.select('td')
        name = dLi[0].text.strip()
        number = dLi[2].text.strip()

        print(name, '-', number)