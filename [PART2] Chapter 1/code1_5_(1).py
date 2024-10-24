birth = int(input("생일을 입력해 주세요. : "))
year = birth // 10000
month = (birth % 10000) // 100
day = birth % 100
print(year, "년", month, "월", day, "일 생이네요!")