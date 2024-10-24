movies = ["미비포유", "해리포터", "맘마미아", "어바웃타임", "라라랜드"] 
print("===========영화 목록===========")
for i in movies: 
  print(i)
print("==============================")
  
choice = input("예매할 영화를 선택해 주세요. : ") 
while choice not in movies:
  print("예매할 수 없는 영화입니다.")
  choice = input("예매할 영화를 선택해 주세요. : ") 
  
print(f"{choice}를 선택했습니다.") 
check = False 

while(not(check)):
  people = float(input("관람 인원수를 입력해 주세요. : ")) 
  if people < 0: 
    print("관람 인원수는 양수만 입력 가능합니다.")
  elif(people % 1) > 0: 
    print("관람 인원수는 정수만 입력 가능합니다.")
  else:
    people = int(people)
    check = True 

print(f"관람할 인원 수는 {people}명입니다.")
  
coupon_dic= {'학생할인' : 3000, '지역할인' : 4000, '회원할인' : 5000} 
process = True 
usage = input("할인권을 사용하려면 y, 금액 확인으로 넘어가려면 n을 입력해 주세요. : ") 
while process:
  if usage == 'y': 
    coupon= input("할인권 이름을 입력해 주세요. : ")
    if coupon in coupon_dic.keys():
      sale = coupon_dic[coupon] 
      print("%d원 할인됩니다." % sale) 
      process= False 
    else:
      print('존재하지 않는 할인권입니다.')
      usage = input('할인권을 다시 입력하려면 y, 아니면 n을 입력해 주세요. : ')
  elif usage == 'n':
    sale = 0
    print('할인권을 사용하지 않았습니다.')
    process = False
  else:
    usage= input('잘못된 입력입니다. 다시 입력해 주세요. : ')
    
origin_price = 12000 * people 
sale_price = sale * people 
total_price = origin_price - sale_price 

print("")
print("<예매 상세 내역>")
print("==============================")
print(f'영화 제목: {choice}')
print(f'관람 인원: {people}명')
print(f'합계 금액: {origin_price}원')
print(f'할인 금액: {sale_price}원')
print("------------------------------")
print(f'실 결제액: {total_price}원')
print("==============================")