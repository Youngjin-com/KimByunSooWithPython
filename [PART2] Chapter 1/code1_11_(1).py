numbers = []
for i in range(7):
  x = int(input("정수를 입력해 주세요. : "))
  numbers.append(x)
result = 0
for num in numbers:
  result += num
print("평균 :", result / 7)