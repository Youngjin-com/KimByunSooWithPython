month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_list = ['금', '토', '일', '월', '화', '수', '목'] 
# 1월 1일이 토요일이므로 day_list[1]='토', day_list[2]='일', ..., day[0]='금'
print("< 2022년 요일 검색 프로그램 >")
a = int(input("월 : "))
b = int(input("일 : "))
if (a in range(1, 13)) and (b in range(1, month_list[a - 1] + 1)):
  total = b
  for i in range(a - 1): 
    total += month_list[i] 
  day = day_list[total % 7]  
  print(f"=> 2022년 {a}월 {b}일은 {day}요일입니다.") 
else: 
  print("=> 존재하지 않는 날짜입니다.")