time = input("24시 기준의 시간을 입력해 주세요. : ").split(':')
hour = time[0] 
miunet = time[1] 
a = int(hour)
if 12 < a < 24:
  print("변환 시간: {}:{} PM".format((int(hour) - 12),miunet))
elif a < 12:
  print("변환 시간: {}:{} AM".format(hour,miunet))
elif a > 24 or a < 0:
  print("잘못된 숫자를 입력했습니다.")
else:
  print("변환 시간: {}:{} PM".format(hour,miunet))