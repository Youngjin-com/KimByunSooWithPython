menu = {
  "물": 700,
  "콜라": 1000,
  "사이다": 1000,
  "과일 주스": 800
}
stock = {
  "물": 5,
  "콜라": 0,
  "사이다": 3,
  "과일 주스": 5
}
print("========= 음료수 목록 =========")
print(" 물\t\t\t {}원".format(menu["물"]))
print(" 콜라\t\t\t{}원".format(menu["콜라"]))
print(" 사이다\t\t\t{}원".format(menu["사이다"]))
print(" 과일 주스\t\t {}원".format(menu["과일 주스"]))
print("===============================")
money = int(input("자판기에 넣을 금액을 입력해 주세요. : "))
choice = input("마시고 싶은 음료를 입력해 주세요. : ")
print(f"{choice}의 가격은 {menu[choice]}원입니다.")
if money < menu[choice]:
  print("돈이 부족합니다.")
else:
  if stock[choice] >= 1:
    print("주문이 완료되었습니다.")
    print("잔액은 {}원입니다.".format(money- menu[choice]))
  else:
    print("현재 해당 음료는 품절 상태입니다.")