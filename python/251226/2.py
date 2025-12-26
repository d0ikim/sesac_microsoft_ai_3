"""# 사후검사 while문
# 기본적으로 Python은 사후검사 루프용 구문을 갖고있지 않다.
i = 1
while True: # 무한 반복 조건식
    print(i)
    i += 1
    if i > 10: break    # 탈출 조건식"""
    
"""# for ~ in range()문
for i in range(0,11,1): # 시작값, 종료값, 증가값
    print(i)

for i in range(0,11):   # 시작값, 종료값
    print(i)

for i in range(11): # 종료값
    print(i)

a = 10
b = 0
for i in range(a, b, -2):
    print(i)"""
    
"""# 0부터 N까지 제곱근 계산하기
import math
n = int(input("정수를 입력하여라: "))
for i in range(n+1):    # range(k)의 기본 동작 → 0부터 시작해서 k-1까지 숫자를 하나씩 만들어 줌
    print(math.sqrt(i))"""
    
# N개 정수를 입력받고, 평균을 계산하고 출력하기
n = int(input("입력할 정수의 개수를 입력하여라: "))
total = 0

for i in range(n):
    num = int(input(str(i+1)+"번째 정수를 입력하여라: "))
    total += num

if n > 0:
    average = total / n
    print("평균:", average)
else:
    print("입력된 정수가 없습니다.")