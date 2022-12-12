# Ex02_csv.py
import csv

# csv 파일 -> 엑셀에서 열림 + 일반 에디터에서 열림
# Common String Value

data = [[1, '김', '책임'],
        [2, '박', '선임'],
        [3, '맹', '연구원']]
import csv
# 읽으려면 r(ead), 쓰려면 w(rite)
# with open('./data/imsi.csv', 'wt', encoding='utf-8') as f:
#     #f.write(data)
#     cout = csv.writer(f)
#     cout.writerows(data)

result = []
with open('./data/imsi.csv', 'rt', encoding='utf-8') as f:
    cin = csv.reader(f)
    result = [row for row in cin if row]    # row가 [] 이렇게 비어 있으면 False

print(result)