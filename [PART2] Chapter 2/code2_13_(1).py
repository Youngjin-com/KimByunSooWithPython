def where_max(num):
  temp_max = 0
    
  for i in range(1, len(num)):
    if num[i] > num[temp_max]:
      temp_max = i
  return temp_max
lst = [10, 55, 66, 81, 10, 50, 78]
print(where_max(lst))