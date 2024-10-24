birth = int(input("생일을 입력해 주세요. : ")) 
year = birth // 10000 
month = (birth % 10000) // 100 
day = birth % 100 
print(str(year) + "년") 
print(str(month) + "월") 
print(str(day) + "일") 