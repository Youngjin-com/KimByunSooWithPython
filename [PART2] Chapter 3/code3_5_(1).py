w_lst = []
count = 0
word = input()
w_lst.append(word)
while True:
  word = input()
  if word[0] != w_lst[count][-1]:
    print("틀린 단어를 입력하셨습니다. 게임을 종료합니다.")
    break
  if word in w_lst: 
    print("앞에서 사용한 단어와 동일한 단어를 입력하셨습니다. 게임을 종료합니다.")
    break
  if(count + 1) % 5 == 4: 
    print("(중간 점검) 현재 %d개의 단어를 입력하셨습니다." % (count + 2))
  w_lst.append(word) 
  count += 1