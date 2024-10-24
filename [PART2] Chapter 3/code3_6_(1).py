def reverse(x): 
  x = list(str(x)) 
  x.reverse() 
  rx = ''.join(x)
  return int(rx) 
def is_prime(x):
  for i in range(2, x + 1): 
    prime = True 
    for j in range(2, i): 
      if i% j == 0: 
        prime = False
        break
  return prime 
    
num = int(input("입력받을 숫자의 개수를 입력해 주세요. : ")) 
lst = []
for i in range(num):
  temp = int(input("%d번째 숫자를 입력해 주세요. : " % (i + 1))) 
  lst.append(temp)
for i in lst: 
  if is_prime(reverse(i)):
    print(i, end= " ")