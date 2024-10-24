num = int(input("숫자를 입력해 주세요. : "))
fac = 1 
for i in range(1, num + 1): 
  fac *= i
print("%d!은 %d입니다." % (num, fac))