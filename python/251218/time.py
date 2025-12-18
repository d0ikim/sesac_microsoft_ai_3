number = int(input("경과 시간(초)를 입력 "))

days, r = divmod(number, 86400) # 60 * 60 * 24
hours, r = divmod(r, 3600)       # 60 * 60
minutes, seconds = divmod(r, 60)

print(days, "일", hours, "시간", minutes, "분", seconds, "초")