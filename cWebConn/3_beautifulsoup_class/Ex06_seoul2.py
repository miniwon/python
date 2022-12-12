from urllib import request
from bs4 import BeautifulSoup

html = 'http://www.seoul.go.kr/seoul/autonomy.do'
site = request.urlopen(html)
site1=site.read()

soup = BeautifulSoup(site1,"html.parser")
구청이름=[temp.text for temp in soup.select('.tabcont strong')];
구청주소=[temp.text for temp in soup.select('.tabcont li:first-child')];
구청전화번호=[temp.text for temp in soup.select('.tabcont li:nth-of-type(2)')];
구청홈페이지=[temp.text for temp in soup.select('.tabcont li:nth-of-type(3)')];

for a, b, c, d in zip(구청이름, 구청주소, 구청전화번호, 구청홈페이지):
 print('구청이름 : {}\n구청주소 : {}\n구청전화번호 : {}\n구청홈페이지 : {}'.format(a, b, c, d));
