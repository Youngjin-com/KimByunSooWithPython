a = input("문장을 입력해 주세요. : ") 
b = a.split('.') 
for i in range(len(b) - 1): 
  c = b[i].strip()      
  d = c.split(' ')    
  for j in range(len(d)): 
    d[j] = d[j].lower() 
    if d[j] == 'i': 
      d[j] = 'I'        
    elif d[j][0:2] == "i'":
      d[j]= d[j].replace('i', 'I') 
  d[0] = d[0].capitalize()
  d = ' '.join(d)
  print(d, end= '. ') 