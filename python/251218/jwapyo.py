import math

print("점 a의 좌표를 입력하시오.")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("점 b의 좌표를 입력하시오.")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

x_temp = (x1 - x2) **2
y_temp = (y1 - y2) **2

d = math.sqrt(x_temp + y_temp)
print("두 점 사이의 거리는 ", d)