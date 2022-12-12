
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

for entry in e:     # a는 반복이 안되지만 b부터 e까지는 반복된다.
    print(entry)
# 문자열도 집합으로 취급하여 하나씩 뽑는다


# 딕셔너리인 경우
for entry in e:
    print(entry, e[entry])
else:   # for문은 무언가가 true니까 돌아가는 것 -> true인 동안 출력 -> 끝나면 false
    print('End')

# 1부터 10까지의 합 구하기
'''
int sum = 0;
for (int i = 1; i <= 10; i++) {
    sum += i;
}

for <타겟 변수> in 집합 객체:
    문장들
'''
sum = 0
for i in range(1, 11):  # 1부터 11-1까지를 i라는 변수에 담아라
    sum += i
print('1부터 10까지의 합계: ', sum)

# 1부터 10까지의 홀수의 합 구하기
sum = 0
for i in range(1, 11, 2):  # 1부터 11-1까지를 2씩 건너뛰어 i라는 변수에 담아라
    sum += i
print('1부터 10까지 홀수의 합계: ', sum)


"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
for i in range(2, 10):  # 2부터 10-1까지를 i라는 변수에 담아라
    print('-'*10, i, '단')
    for j in range(1, 10):
        print(i, '*', j, '=', i*j)


li = ['z', 'x', 'y']
while li:
    data = li.pop()
    print(data)
else:
    print('End')
# li의 요소들을 뒤에서부터 pop하여 li에는 남은 요소가 없게 된다
