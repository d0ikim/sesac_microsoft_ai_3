"""# 4개 숫자의 총합 구하기
i = 1
total = 0
while i <= 4:   # 반복 조건식
    num = int(input(f"숫자 {i}를 입력하세요: "))
    total += num
    i += 1  # i 증가식
print("총합:", total)"""

"""# 숫자 N개의 곱 구하기
i = 1
total = 1
n = int(input("몇 개의 숫자를 곱하시겠습니까? "))
while i <= n:   # 반복 조건식
    num = int(input(f"숫자 {i}를 입력하세요: "))
    total *= num
    i += 1  # i 증가식
print("총곱:", total)"""

"""# 20개의 정수를 입력받아 그중 홀수의 합 구하기
total = 0
i = 1
while i <= 20:   # 반복 조건식
    a = int(input(f"정수 {i}를 입력하세요: "))
    if a%2 != 0:
        total += a
    i += 1  # i 증가식
print("홀수의 합:", total)"""