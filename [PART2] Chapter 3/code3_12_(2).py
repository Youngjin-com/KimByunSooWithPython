print("< 회문 판단 프로그램 >\n")

letter = []
word = input("단어를 입력해 주세요. : ")

for i in word:
  letter.append(i)

rev_letter = list(reversed(letter))

if letter == rev_letter:
  result = "회문입니다."
else:
  result = "회문이 아닙니다."
print("판단 결과 :", result)