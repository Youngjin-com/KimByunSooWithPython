num = input("숫자를 입력해 주세요. : ")
List = num.split('.') 
under = list(List[1])
if(float(under[0]) < 5): 
  x = List[0]
else: 
  x = int(List[0])
  x += 1

print(x)