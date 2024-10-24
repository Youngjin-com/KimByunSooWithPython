given_lst = []
count = 1
sum = 0
while count <= 7:
  given_lst.append(int(input("정수를 입력하세요. : ")))
  sum += given_lst[count - 1]
  count += 1

average = sum / 7
print("평균: ", average)