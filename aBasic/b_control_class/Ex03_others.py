msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

# -----------------------------------
# (1) unpacking: 요소 분해
'''
    a = msg[0]
    b = msg[1]
    c = msg[2]
'''
a, b, c = di
print(a)
print(b)
print(c)

alist = [(1, 2), (3, 4), (5, 6)]
for temp in alist:
    print(temp)     # 튜플 한 덩어리씩 출력

for first, second in alist:
    print("{} + {} = {}".format(first, second, first+second))

# -----------------------------------
# (2) enumerate() 함수
'''
    [참고] 자바에서
        Iterator -> Enumerator(이전 버전)
'''
blist = ['개발자', '코더', '전문가', '노가다']
for value in blist:
    print(value)

for value in enumerate(blist):
    print(value)

for idx, value in enumerate(blist):
    print(idx, value)

# ----------------------------------
# (3) zip() 함수
days = ['월', '화', '수']
doit = ['잠자기', '밥먹기', '숨쉬기', '멍때리기']

print(zip(days, doit))
print(list(zip(days, doit)))
print(dict(zip(days, doit)))

for day, todo in zip(days, doit):
    print(day, todo)

month = [11, 12, 1]
print(list(zip(days, doit, month)))