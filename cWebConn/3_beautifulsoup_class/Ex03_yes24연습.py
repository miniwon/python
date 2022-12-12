
from bs4 import BeautifulSoup
from urllib import request

html = request.urlopen("http://www.yes24.com/Product/Search?domain=ALL&query=python")

soup = BeautifulSoup(html, 'html.parser')

# [1]
infos = soup.select('#yesSchList li')

for info in infos:
    print(info.select_one('a.gd_name').text)
    
print(len(infos), "권이 검색되었습니다")


# [2]
imgUrls = soup.select("#yesSchList div.itemUnit img")
# print(imgUrls)

for imgUrl in imgUrls:
    # 책 제목을 출력: alt
    bookName = imgUrl.attrs['alt'].strip().replace("/", "_")
    # 이미지 링크를 출력: src
    imgPath = imgUrl.attrs['data-original']
    print(bookName, imgPath)
    request.urlretrieve(imgPath, 'imgs/' + bookName + '.png')
