def rsp_num_name(a): 
  if a == 1: 
    return "가위" 
  elif a == 2:
    return "바위"
  else: 
    return "보"
def rsp_name_num(rsp):
  if rsp == "가위":
    return 1
  elif rsp == "바위":
    return 2
  else:
    return 3
def rsp_winner(a, b):
  return a - b

import random 
n = random.randint(1, 3) 
you = input("가위바위보 게임입니다. 무엇을 낼지 입력해 주세요. : ")
print("사용자:", you) 
print("컴퓨터:", rsp_num_name(n)) 
w = rsp_winner(rsp_name_num(you),n) 
if w == 0:
  print("비겼습니다.")
elif w == 1 or -2:  
  # 숫자 차이가 1 또는 -2일 때 이김. 예를 들어, 사용자가 가위(1)이고 컴퓨터가 보(3)일 때 w 값은 1 - 3 = -2가 됨
  print("축하합니다. 당신이 이겼습니다.")
else:
  print("당신이 졌습니다.")