num = int(input("숫자를 입력해 주세요. : "))  
sum = 1 
a= 1   
while a <= num:
  sum = sum * a
  a += 1
  
print("%d!은 %d입니다." % (num, sum))