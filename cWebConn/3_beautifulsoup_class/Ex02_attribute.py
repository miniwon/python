from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <ul>
                <li><a href='http://www.naver.com'>네이브</a></li>
                <li><a href='http://www.daum.net'>다아음</a></li>
            </ul>
        </body>
    </html>
"""

''' 리스트(li)목록의 내용과 해당 경로를 추출하기
    속성추출 : attrs['속성명']

    [출력결과]
    네이브 : http://www.naver.com
    다아음 : http://www.daum.net
'''

# 1. 데이터 파싱
soup = BeautifulSoup(html, 'html.parser')

# 2. 원하는 요소 접근하기
# tags = soup.ul.children
# print(tags)
# for aTag in tags:
#     print(aTag)

aTags = soup.findAll('a')
print(aTags)

# 3. 요소의 내용 추출하기
for aTag in aTags:
    print(aTag.text)
    print(aTag.attrs['href'])
