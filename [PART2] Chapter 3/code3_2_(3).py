num = input("각 숫자를 공백으로 구분하여 입력해 주세요. : ").split()
a = 0
b = 0
for i in num:
  sum = 0
  for j in i:
    sum += int(j)
    if sum > a:
      a = sum
      b = i
print(b)