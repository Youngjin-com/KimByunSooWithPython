num_list = []
sum = 0
for i in range(0, 7):
  num_list.append(int(input("정수를 입력하세요. : ")))
  sum = sum + num_list[i]
print("평균 :", sum / 7)