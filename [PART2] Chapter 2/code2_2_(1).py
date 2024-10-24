a = input("문장을 입력해 주세요. : ")  
b = a.split(' ') 
b = set(b) 
b = list(b)
b.sort()
for i in b:
  print(i, end= ' ')