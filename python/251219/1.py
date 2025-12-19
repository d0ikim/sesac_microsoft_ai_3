"""# 문자열 대체하기 [문자열.replace(a, b)]
# a : 바꾸려는 이전 내용(문자열 내용 중에서 찾는다)
# b : 바꿀 새로운 내용
a = "I am rewbie in Java. Java rocks!"
b = a.replace("Java", "Python")
print(b)"""

"""# 문자열 내 문자 개수 세기 [len(문자열)]
a = "Hello Olympians!"
print(len(a))   # 16
b = "I am newbie in Python"
k = len(b)
print(k)    # 21"""

"""# 문자열 위치 찾기 [문자열.find(a)]
# 주어진 문자열 안에서 찾으려는 내용(a)이 시작하는 위치를 반환
a = "I am newbie in Python. Python rocks!"
i = a.find("newbie")
print(i)    # 5"""

"""# 소문자로 바꾸기 [문자열.lower()]
a = "My NaMe is JohN"
b = a.lower()
print(b)    # my name is john"""

"""# 대문자로 바꾸기 [문자열.upper()]
a = "My NaMe is JohN"
b = a.upper()
print(b)    # MY NAME IS JOHN"""

"""# 소문자열 가져오기 [string.ascii_lowercase]
# string 모듈에서 소문자열 값(a~z)을 가져온다
# string 모듈을 임포트해야 한다
import string
print(string.ascii_lowercase)   # abcdefghijklmnopqrstuvwxyz"""

"""# 대문자열 가져오기 [string.ascii_uppercase]
# string 모듈에서 대문자열 값(A~Z)을 가져온다
# string 모듈을 임포트해야 한다
import string
print(string.ascii_uppercase)   # ABCDEFGHIJKLMNOPQRSTUVWXYZ"""

"""# 로그인 ID 생성하기
# 이름을 입력받고, 소문자로 변환 후, 정수 3개를 추가하여 로그인 ID를 만든다
import random
lower_name = input("영문이름을 입력하세요: ").lower()[:5]   # 소문자로 변환 후, 앞에서 5글자까지 가져오기
random_int = random.randrange(100, 1000)    # 100~999 사이의 정수 난수 생성
login_id = lower_name + str(random_int)
print(login_id)"""

"""# 랜덤 단어 생성하기(변형)
# 다섯개의 문자로 이루어진 랜덤 단어를 출력한다
# 소문자 상수를 가져온다 -> 임의의 문자를 선택한다 -> 결과 출력
import random
import string
alphabet = string.ascii_lowercase
random_word = alphabet[random.randrange(26)] + \
            alphabet[random.randrange(len(alphabet))] + \
            alphabet[random.randrange(len(alphabet))] + \
            alphabet[random.randrange(len(alphabet))] + \
            alphabet[random.randrange(len(alphabet))]
print(random_word)  # vxxog, fdubr, uuzvk, efotp, aiymy, gzdhk"""

