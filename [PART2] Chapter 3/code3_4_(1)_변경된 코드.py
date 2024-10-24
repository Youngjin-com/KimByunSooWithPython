a = input("숫자 두 개를 입력해 주세요.(예: '3 5') : ")
numbers = a.split(' ') 
b = int(input("배수를 알고 싶은 숫자를 입력해 주세요. : ")) 

num1 = int(numbers[0]) 
num2 = int(numbers[1]) 
for i in range(num1, num2 + 1): 
  if i % b == 0: 
    print(i, end = ' ')