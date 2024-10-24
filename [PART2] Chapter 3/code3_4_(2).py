num = input('숫자 두 개를 입력해 주세요.(예: \'3 5\') : ')
n = int(input('배수를 알고 싶은 숫자를 입력해 주세요. : '))
num1, num2 = map(int, num.split())
print(f'\n[{num1} 이상 {num2} 이하인 {n}의 배수]')
if n > num2: 
  print('Not Exist')
else:  
  cnt = 0
  print('=>', end=' ')
  for i in range(num1, num2 + 1):
    if i% n == 0:
      print(i, end=' ')
      cnt += 1
  print(f'\n=> 총 {cnt}개')