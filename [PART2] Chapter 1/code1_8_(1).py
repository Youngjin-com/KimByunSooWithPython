count = 0
for i in range(1, 101):
  if i % 2 == 0 and i % 7 != 0:
    count = count + 1
print(count)