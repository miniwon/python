"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""

# import urllib
from urllib import parse

baseUrl = 'http://www.example.com/html/a.html'

print(parse.urljoin(baseUrl, 'b.html'))

print(parse.urljoin(baseUrl, 'sub/c.html'))
    # 상대 경로: 현재 위치에서 /sub/

print(parse.urljoin(baseUrl, '/sub/d.html'))
    # 절대 경로: 최상위 위치에서 /sub/

print(parse.urljoin(baseUrl, '../temp/e.html'))
    # 상대 경로: 상위 폴더로 가서