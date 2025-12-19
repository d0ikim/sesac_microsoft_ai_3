"""# 할인액 계산하기
amount = float(input("주문액을 입력하여라: "))
if amount>=150000:
    discount = 20
elif amount>=70000:
    discount = 10
elif amount>=30000:
    discount = 5
else:
    discount = 0"""
    
"""# 윤년 계산하기
import re   # 정규식 모듈 임포트
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"    # 정수 또는 실수를 판별하는 정규식

year = input("연도를 입력하세요: ")
if not re.match(IS_NUMERIC, year):   # 파이썬에서는 비정상 먼저 걸러내고
    print("숫자가 아닙니다.")
else:   # 정상은 else에서 처리
    year = int(year)
    if year%4==0 and year%100!=0 or year%400==0:
        print(year,"년은 윤년입니다.")"""

"""# while-루프
i = 1
while i<=10:
    print(i)
    i+=1"""
    
