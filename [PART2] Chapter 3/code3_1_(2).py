sentence = input('문장을 입력해 주세요. : ')
sentence = sentence.lower().split('. ')
answer = []
for s in sentence:
  s = s.capitalize() #첫 글자 대문자
  if s in "i'":
    s = s.replace("i'","I'")
    answer.append(s)
  elif s in " i ":
    s = s.replace(" i "," I ")
    answer.append(s)
  elif s in " i":
    s = s.replace(" i"," I")
    answer.append(s)
  elif s in "i ":
    s = s.replace("i ","I ")
    answer.append(s)
  else:
    answer.append(s)
print('. '.join(answer))