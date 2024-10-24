a = 3420
print(a)

b = a //1000
c = a //100 - (b * 10)
d = a //10 - (c * 10) - (b * 100)
print("1000원 :", b)
print("100원 :", c)
print("10원 :", d)
print("필요한 동전의 개수 :", c + d)