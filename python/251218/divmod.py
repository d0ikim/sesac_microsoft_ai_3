number = int(input("다섯 자리 정수를 입력 "))

d1= number // 10000
r = number % 10000

d2 = r // 1000
r = r % 1000

d3 = r // 100
r = r % 100

d4 = r // 10

d5 = r % 10

total = d1 + d2 + d3 + d4 + d5
print("합:",total)