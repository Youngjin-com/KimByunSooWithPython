lst = [] 
for i in range(5):
  a = int(input("숫자를 입력하세요. : "))
  lst.append(a) 
for i in range(0, len(lst) - 1): 
  min_i = i
  for j in range(i + 1, len(lst)): 
    if lst[j] < lst[min_i]:
      min_i= j 
  lst[i], lst[min_i] = lst[min_i], lst[i]
print(lst)