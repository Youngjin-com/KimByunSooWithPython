height = int(input("삼각형의 높이를 입력해 주세요. : "))
for i in range(1, height + 1):
  print(' ' * (height - i) + '*' * i)