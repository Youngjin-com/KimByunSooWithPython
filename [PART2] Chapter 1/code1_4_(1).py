total = 3420
a = total // 1000
b = (total % 1000) // 100
c = (total % 100) // 10
print(total, "원을 계산하려면")
print("1000원 지폐", a, "장")
print("100원 동전", b, "개")
print("10원 동전", c, "개가 필요합니다.")