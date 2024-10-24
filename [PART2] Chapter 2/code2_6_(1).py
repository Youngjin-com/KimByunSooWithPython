answer= list(input("퀴즈 결과를 입력해 주세요.(예: OOXOXXO): "))
total = 0
current = 1 
for i in answer:
  if i == 'O':
    total += current 
    current += 1
  elif i == 'X':
    if current > 1:
      current = 1
  
print(total)