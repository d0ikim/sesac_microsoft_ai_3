"""# 숫자가 동시에 5와 8로 나누어 떨어지는지 검사하기
import re   # 정규식 모듈 임포트
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"    # 정수 또는 실수를 판별하는 정규식
inp = input("정수를 입력하여라: ")
if re.match(IS_NUMERIC, inp):   # 입력이 숫자인지 판별
    x = int(inp)
    if x%5==0 and x%8==0:
        print(x, "는 5와 8로 나누어 떨어집니다.")
    else:
        print(x, "는 당신이 찾는 숫자가 아닙니다.")
else:
    print("숫자가 아닙니다.")"""
    
"""# 차량 통행료 받기
# 톨게이트 통과하는 차종을 입력받고 차종에 M(오토바이), C(승용차), T(트럭) 따라 요금을 출력한다.
# 잘못 입력되면 오류메시지를 출력한다.
v = input().upper()   # 대문자로 변환
if v=='M':
    print("통행료는 1000원입니다.")
elif v=='C':
    print("통행료는 2000원입니다.")
elif v=='T':
    print("통행료는 3000원입니다.")
else:
    print("차종을 잘못 입력하셨습니다.")"""
    
"""# 일차방정식 ax+b=0 풀기
# 방정식 ax+b=0의 근을 구한다.
# x=-b/a
# a가 0인 경우의 처리를 고려
a = float(input("a값을 입력하여라: "))
b = float(input("b값을 입력하여라: "))
if a!=0:
    x=-b/a
    print(x)
elif b!=0:
    print("해가 없습니다.")
else:
    print("항등식")"""