def getSum(num):
  return num * (num + 1) // 2
n = int(input('정수를 입력하세요. : '))
result = getSum(n)
print(result)