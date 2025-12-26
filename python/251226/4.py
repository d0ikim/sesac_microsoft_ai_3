"""# 구구단 출력하기
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j, end = "\t")
    print()  # 줄바꿈"""

""" # 24시간 인사 출력하기
for hour in range(1, 25):
    print("현재 시간은", hour, "시입니다.")
    if hour >= 4 and hour < 12:
        print("좋은 아침입니다.")
    elif hour >= 12 and hour < 20:
        print("좋은 오후입니다.")
    elif hour >= 20 and hour < 24:
        print("좋은 저녁입니다.")
    else:
        print("편히 주무세요.")"""
        
s = 0
i = 1
while True:
    s += i
    if i == 101: break
print("1부터 100까지의 총합:", s)