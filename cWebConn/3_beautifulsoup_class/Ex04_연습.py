from bs4 import BeautifulSoup
from urllib import request
import os
from urllib import request, parse


# [1] 녹색 글자만 추출하여 출력
html = request.urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
soup = BeautifulSoup(html, 'html.parser')

greens = soup.select('.green')

for green in greens:
    print(green.text)

print('-'*50)

# [2] 아이템과 가격을 추출
html = request.urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, 'html.parser')

trs = soup.select('#giftList .gift')

for tr in trs:
    print('item:', tr.select('td')[0].text, 'price:', tr.select('td')[2].text)


# [3-1] 책 제목과 저자만 추출
html = request.urlopen("https://wikidocs.net/")
soup = BeautifulSoup(html, 'html.parser')

books = soup.select('div#books .book-item .col-sm-6')

for book in books:
    print(book.select_one('a.book-subject').text, '-', book.select_one('a.menu_link').text, '지음')

# [3-2] 이미지 다운로드
imgUrls = soup.select("img.book-image")

for book in books:
    bookName = book.select_one('a.book-subject').text
#    imgPath = 'https://wikidocs.net' + book.select_one("img.book-image").attrs['src']
    i = parse.quote_plus(parse.urljoin('https://wikidocs.net', book.select_one("img.book-image").attrs['src']), safe="://")  # url 한글깨짐 문제 해결 : quote_plus 사용
    print(bookName, i)

    request.urlretrieve(i, 'prac_imgs/' + bookName + book.select_one("img.book-image").attrs['src'][-4:])

# from urllib.parse import quote_plus
# from bs4 import BeautifulSoup
# import os
# from urllib import request, parse
#
# os.makedirs('wikiImage', exist_ok=True)
#
# url='https://wikidocs.net/'
# html = request.urlopen(url)
#
# soup = BeautifulSoup(html,'html.parser')
# titles = soup.select('#books .book-subject')
# author = soup.select('#books .book-detail .menu_link')
# imgs = soup.select('#books .book-image')
#
# for i in imgs:
#     print(i.attrs['src'])
#
# for t, a in zip(titles, author):
#     print("책제목 : ",t.text, " - 책 저자 : ",a.text)
#
# for i, t in zip(imgs, titles):
#     try:
#         request.urlretrieve(parse.urljoin(url,i.attrs['src']),'./wikiImage/{}.png'.format(t.text))
#     except UnicodeEncodeError:
#         i = quote_plus(parse.urljoin(url,i.attrs['src']),safe="://")
#         request.urlretrieve(i,'./wikiImage/{}.png'.format(t.text))
# print(len(titles))
