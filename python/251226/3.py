"""a = 1
i = 5

while i < 7:
    for j in range(1, 5, 2):
        a = a * j + i
    i += 1
print(a)"""

s = 'I have a dream'
letter = input('검색할 영문자를 입력하여라: ')
found = False

"""# for문
for a in s:
    if a == letter:
        found = True"""
"""# while문 (break를 사용하지 않는 방법)
i = 0
while i <= len(s) -1 and found == False:
    if s[i] == letter:
        found = True
    i += 1"""
"""if found == True:
    print('문자', letter, '을 찾았습니다.')"""
# if ~ in Seq (가장 파이썬 다운 방법)
if letter in s:
    print("문자", letter, "을 찾았습니다.")

