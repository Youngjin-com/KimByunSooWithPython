num = int(input("숫자를 입력해 주세요. : "))
d = 2
while d <= num:
  if num % d == 0:
    print(d, end=" ")
    num /= d
  else:
    d = d + 1