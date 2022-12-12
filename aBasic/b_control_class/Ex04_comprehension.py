"""
    @ 컴프리헨션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컴프리헨션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔너리 컴프리헨션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컴프리헨션
        { 표현식 for 표현식 in 순회가능객체 }

"""


# 컴프리헨션 사용하지 않은 리스트 생성
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1, 7):
    alist.append(n)
print(alist)

alist = list(range(1, 7))
print(alist)


#------------------------------------------------
# 리스트 컴프리헨션
blist = [n for n in range(1, 7)]
print(blist)

blist = [n**2 for n in range(1, 7)]
print(blist)

blist = [n for n in range(1, 7) if n % 2 == 1]
print(blist)

# 컴프리헨션 아닌 코드를 컴프리헨션으로 변경
clist = []
for r in range(1, 4):       # [1, 2, 3]
    for c in range(1, 3):   # [1, 2]
        clist.append((r, c))
print(clist)

dlist = [(p, q) for p in range(1, 4) for q in range(1, 3)]
print(dlist)


#-------------------------------------------
# 딕셔너리 컴프리헨션
data = (2, 3, 4)
adic = {n: n**2 for n in data}
print(adic)


#------------------------------------------------
# 셋 컨프리핸션
data = (1, 2, 3, 2, 1, 4, 5)

alist = []
alist = [n for n in data]
print(alist)

bset = {n for n in data}
print(bset)

word = 'LOVE LOL'
wcnt = {letter: word.count(letter) for letter in word}
print(wcnt)

'''
#------------------------------------------------
# 프로젝트할 때 팀구호
우리의결의= """취하고싶으면달려라
             맡은업무는반드시마치자
             노력없는성과는없다
             구글신과함께공부하자"""

result = [ j[i*2] for i, j in enumerate(우리의결의.splitlines())]
print(result)
'''
우리의결의 = """취하고싶으면달려라
맡은업무는반드시마치자
노력없는성과는없다
구글신과함께공부하자
"""
print(enumerate(우리의결의.splitlines()))
result = [j[i*2] for i, j in enumerate(우리의결의.splitlines())]
print(result)
#취, 업, 성, 공

# -------------------------------------------------
# 프로젝트할 때 팀구호
#우리의결의= """취하고싶으면달려라
#맡은업무는반드시마치자
#노력없는성과는없다
#구글신과함께공부하자
#"""
#result = [ j[i*2] for i, j in enumerate(우리의결의.split('\n')]
#print(result)