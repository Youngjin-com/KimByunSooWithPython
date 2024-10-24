def rsp_num(rsp): 
  if rsp == '가위':
    return 1
  elif rsp == '바위':
    return 2
  else:
    return 3
def rsp_result(a, b): 
  gap = a - b
  if gap == 0:
    txt = "비겼습니다."
  elif gap in [-2, 1]:
    txt = "축하합니다. 당신이 이겼습니다."
  else:
    txt = "당신이 졌습니다."
  return txt

import random
rsp_list = ['가위', '바위', '보']

print("< 가위바위보 게임 >")
YOU = input("무엇을 낼지 입력해 주세요. : ")
COM = random.choice(rsp_list) 
print(f"\n당신   : {YOU}")
print(f"컴퓨터 : {COM}\n")

Y = rsp_num(YOU)
C = rsp_num(COM)
result = rsp_result(Y, C)

print("결과 :", result)