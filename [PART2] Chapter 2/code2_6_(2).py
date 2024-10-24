answers = input("퀴즈 결과를 입력해 주세요.(예: OOXOXXO): ").split("X")
score = 0
for n in answers:
  for j in range(0, len(n) + 1):
    score = score + j
print(score)