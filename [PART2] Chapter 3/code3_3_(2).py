month = 8 
start = 1 
last = 31 #총 일수
if start != 0: 
  rest = 7 - start
else: 
  rest= 0
print(f'    < {month}월 달력 >')
print('일 월 화 수 목 금 토')
print(' ' * 3 * start, end='')   
for i in range(1, last + 1):  
  if(i % 7 != rest):  
    print('%2d' % i, end=' ')
  else: 
    print('%2d' % i)