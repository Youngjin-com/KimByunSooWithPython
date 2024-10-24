time = input("24시 기준의 시간을 입력해 주세요. : ")
t = time.split(':') 
if int(t[0]) == 12 and int(t[1]) >= 0: 
  print("변환 시간:", t[0],":", t[1], "PM") 
elif int(t[0]) > 12 and int(t[1]) >= 0: 
  print("변환 시간:", int(t[0]) - 12, ":", t[1], "PM") 
elif int(t[0]) == 0 and int(t[1]) >= 0: 
  print("변환 시간:", 12, ":", t[1], "AM") 
elif int(t[0]) < 12 and int(t[1]) >= 0: 
  print("변환 시간:", t[0],":", t[1], "AM")