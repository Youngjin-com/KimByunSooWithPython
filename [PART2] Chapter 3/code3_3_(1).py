print("\t\t\t<8월 달력>")
start_day = 1  
# 일요일일 경우 start_day = 0, 화요일일 경우 2... , 토요일일 경우 6
last_date = 31 
print('\t일\t월\t화\t수\t목\t금\t토')
for i in range(start_day): 
  print('\t', end='')
for i in range(1, last_date + 1): 
  if(i % 7 != 6):
    print('\t%d' % i, end='')
  elif(i % 7 == 6):
    print('\t%d\n' % i)