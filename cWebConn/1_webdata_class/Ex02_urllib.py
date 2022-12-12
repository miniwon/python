
# 내장 모듈 이용

from urllib import request
url = 'http://www.google.com'
site = request.urlopen(url)

page = site.read()
print(page)
print('-'*50)
print(site.status)
print('-'*50)

headers = site.getheaders()
print(headers)

for header in headers:
    print(header[0], '>>', header[1])