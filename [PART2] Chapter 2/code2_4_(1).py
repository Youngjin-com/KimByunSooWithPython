num = int(input("삼각형의 높이를 입력해 주세요. : "))
for i in range(0, num): 
  for j in range(0, num - 1 - i): 
    print(' ', end='') 
        
  for k in range(0, i + 1):
    print('*', end='') 
  print("")