count = 0
for i in range(1, 101) :
  if(i % 2 == 0) : 
    if(i % 7 != 0) :
      count = count + 1
    else: 
      count = count
  else:
    count = count
print("the number of divided by 2, but not divided by 7 is", count)