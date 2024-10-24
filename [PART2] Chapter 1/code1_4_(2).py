money=3420
print("1000원 :",money//1000)
cnt1=money//1000
money=money%1000
print("100원 :",money//100)
cnt2=money//100
money=money%100
print("10원 :",money//10)
cnt3=money//10
print("필요한 동전의 개수 :", cnt2+cnt3)