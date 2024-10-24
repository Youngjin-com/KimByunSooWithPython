sentence = input("문장을 입력해 주세요: ")
List = sentence.split(' ')  
newList = [] 

for i in List:
  if i not in newList:
    newList.append(i)

newList.sort()

result = " ".join(newList)
print(result)