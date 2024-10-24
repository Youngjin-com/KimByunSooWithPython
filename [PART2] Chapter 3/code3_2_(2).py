numList, sumList= [], []
nums = input("각 숫자를 공백으로 구분하여 입력해 주세요. : ")
numList = nums.split(' ')
for i in numList:
  partial_sum = 0
  for n in i:
    partial_sum += int(n)
  sumList.append(partial_sum)
maxNum = max(sumList)
result = numList[sumList.index(maxNum)]
print(result)