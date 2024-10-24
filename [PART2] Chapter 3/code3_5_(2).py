Words = []
while(True):
  old_len = len(Words)
  w = input()
  if(len(Words) > 0):
    before_word = Words[-1]
    if not(w[0] == before_word[-1]):
      print("틀린 단어를 입력하셨습니다. 게임을 종료합니다.")
      break
  Words.append(w)
  if(old_len == len(set(Words))):
    print("앞에서 사용한 단어와 동일한 단어를 입력하셨습니다. 게임을 종료합니다.")
    break
  if(len(Words) % 5 == 0):
    print(f"(중간 점검) 현재 {len(Words)}개의 단어를 입력하셨습니다.")