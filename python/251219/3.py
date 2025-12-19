"""# 이중-택일 결정 구조 if-else
pay_per_hour = int(input("시급을 입력하세요: "))
hours = int(input("근무 시간을 입력하세요: "))
if hours <= 40:  # 40시간 이하 근무 시
    pay = pay_per_hour * hours
else:   # 40시간 초과 근무 시
    pay = (pay_per_hour * 40) + (pay_per_hour * (hours - 40) * 1.5) # 40시간까지는 시급만 계산 + 초과근무 시간에 대해 1.5배 계산
print("주급은", pay)"""

"""# 다중-택일 결정 구조 if-elif-else
a = int(input())
b = int(input())
if a>3:
    print("변수 a는 3보다 큽니다.")
elif a>2 and b<=10:
    print("변수 a는 4보다 크고")
    print("변수 b는 10보다 작거나 같습니다.")
elif a*2 == -26:
    print("변수 a 곱하기 2는 -26과 같습니다")
    b+=1
elif b==1:
    print("변수 b는 1과 같습니다.")
else:
    print("위의 모든 불리언 식이 False일 경우")
    print("이 메시지가 표시됩니다.")
print("종료!")"""

"""# 숫자 자릿수 세기
x = int(input("정수를 입력하여라(0 - 999): "))
if x<=9:
    count = 1
elif x<=99:
    count = 2
else:
    count = 3
print("자릿수:", count)"""

"""# 요일 출력하기
day = int(input("1과 7 사이의 숫자를 입력: "))
if day==1:
    print("일요일")
elif day==2:
    print("월요일")
elif day==3:
    print("화요일")
elif day==4:
    print("수요일")
elif day==5:
    print("목요일")
elif day==6:
    print("금요일")
elif day==7:
    print("토요일")
else:
    print("부적절한 숫자")"""
    
