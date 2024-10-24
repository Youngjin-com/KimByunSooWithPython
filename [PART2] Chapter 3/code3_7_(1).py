menu = {'물' : [700, 5], '콜라' : [1000, 0], '사이다' : [1000, 3], '과일 주스' : [800, 2]}
print("======음료수 목록======")
print("물\t\t700원")
print("콜라\t\t1000원")
print("사이다\t\t1000원")
print("과일 주스\t800원")
print("======================")
money = int(input("자판기에 넣을 금액을 입력해 주세요. : "))
choice = input("마시고 싶은 음료를 입력해 주세요. : ")
if choice in menu: 
  print("%s의 가격은 %d원입니다." % (choice, menu[choice][0])) 
  if menu[choice][1] == 0: 
    print("현재 해당 음료는 품절 상태입니다.")
  else: 
    if money < menu[choice][0]: 
      print("돈이 부족합니다.")
    else:
      print("주문이 완료되었습니다.") 
      print("잔액은 %d입니다." % (money- menu[choice][0]))
else:
  print("해당 음료가 존재하지 않습니다.")