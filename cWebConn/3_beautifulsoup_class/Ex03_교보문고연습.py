'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import request

# 교보문고 > '파이썬' 검색 > 국내도서
html = urlopen("https://search.kyobobook.co.kr/search?keyword=python&gbCode=TOT&target=total")

soup = BeautifulSoup(html, 'html.parser')

prod_item = soup.select('li.prod_item')
for prod_info in prod_item:
    # print(prod_info)
    imgTag = prod_info.select_one('img')
    bookNumber = imgTag.attrs['data-kbbfn-bid']
    print(bookNumber)
    request.urlretrieve('https://contents.kyobobook.co.kr/pdt/' + bookNumber + '.jpg', 'imgs/kyobobook' + bookNumber + '.jpg')

    print('-----')
    from selenium import webdriver
    from urllib import request

    # chrome의 ...을 눌러 크롬버전을 본다
    # chrome driver를 버전에 맞게 다운로드 : https://chromedriver.chromium.org/downloads
    ## Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
    driver = webdriver.Chrome('C:/Users/kosmo/Downloads/chromedriver')
    driver.get('https://search.kyobobook.co.kr/search?keyword=python&gbCode=TOT&target=total')
    info = driver.find_elements_by_class_name('prod_img_load')
    info2 = driver.find_elements_by_class_name('result_checkbox.spec_checkbox')
    for x, y in zip(info, info2):
        print(y.get_attribute('data-name'), ' : ', x.get_attribute('src'))
        request.urlretrieve(x.get_attribute('src'),
                            'imgs/' + y.get_attribute('data-name').strip().replace('/', '_') + '.jpg')
