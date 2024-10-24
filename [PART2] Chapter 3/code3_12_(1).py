s = input("단어를 입력해 주세요. : ")
front = []
behind = []
result = True

for i in s:
  front.append(i)
  behind.append(i)

start = 0
end = len(behind) - 1

while start < len(behind):
  if front[start] != behind[end]:
    result = False
  start += 1
  end -= 1

if result:
    print("%s는 회문입니다."% (s))
else:
    print("%s는 회문이 아닙니다."% (s))