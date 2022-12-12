f = open('./data/sample.json', 'rt', encoding='utf-8')
data = f.read()
f.close()

print(data)
print(type(data))

import json
items = json.loads(data)

print(items)
print(type(items))

sum = 0
for k, val in items.items():
    sum += val['price'] * val['count']
    print(k, '의 총합:', val['price'] * val['count'], '원')

print('모든 상품의 총합:', sum, '원')