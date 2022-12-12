"""
@ 네이버 금융에서 환률 정보 가져오기

` 크롬에서 네이버 > 금융 > 시장지표 > 미국 USD 금액을 부분을 개발자 모드로 확인
      <div class='head_info'>
         <span class='value'>1.098.50</span>
"""


from bs4 import BeautifulSoup
from urllib import request as req


# 웹 문서 가져오기
url = 'https://finance.naver.com/marketindex/'
res = req.urlopen(url)
print(res)

# 파싱하기
soup = BeautifulSoup(res, 'html.parser')

# 추출하기
li = soup.select("#exchangeList li")
for value in li:
    # print(value)
    print( value.select_one('h3.h_lst').text, ":", value.select_one('span.value').text, '원')

print('-'*50)

# exchangeValue = soup.select("#exchangeList span.value")
# exchangeNation = soup.select("#exchangeList h3.h_lst")

# for i in range(len(exchangeNation)):
#     print(exchangeNation[i].text, ": ", exchangeValue[i].text)

# 정인
mm = soup.select('#exchangeList li')

# print('달러 : ', usd.text)
for m in mm:
    name = m.select_one('h3.h_lst')
    f = m.select_one('span.value')
    print(name.text, ':', f.text)