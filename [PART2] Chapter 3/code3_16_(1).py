month = int(input("월 : "))
date = int(input("일 : "))
dnjf = month
dlf = date
month -= 1
a = '요일'
while month > 0:
  if month % 2 == 0:
    if month < 8 and month != 2:
      date += 30
    elif month == 2:
      date += 28
    else:
      date += 31
  else:
    if month < 8:
      date += 31
    else:
      date += 30
  month -= 1
if date % 7 == 0:
  a = '금'
if date % 7 == 1:
  a = '토'
if date % 7 == 2:
  a = '일'
if date % 7 == 3:
  a = '월'
if date % 7 == 4:
  a = '화'
if date % 7 == 5:
  a = '수'
if date % 7 == 6:
  a = '목'
print("%s월 %s일은 %s요일입니다." % (dnjf, dlf, a))