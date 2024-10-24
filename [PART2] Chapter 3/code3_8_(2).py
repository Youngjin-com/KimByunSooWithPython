total, minute, second= 0, 0, 0
while(1) :
  n = int(input("원하는 버튼의 숫자를 입력해 주세요. : "))
  if n == 1:
    total += 10
  elif n == 2:
    total += 30
  elif n == 3:
    total += 60
  elif n == 4:
    total += 600
  elif n == 5:
    break
  else:
    print("잘못된 입력입니다.")
  if total <  60:
    print("00:%d" % total)
  elif total >= 60:
    minute = (total // 60)
    second = (total % 60)
    print("%d:%02d" % (minute, second))
print("\n전자레인지를 작동합니다.")