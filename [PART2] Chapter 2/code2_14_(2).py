time = int(input("시간(초)을 입력해 주세요. : "))
converted = []
day = time // 86400
converted.append(day)
hour = (time % 86400) // 3600
converted.append(hour)
minute = (time % 3600) // 60
converted.append(minute)
second = time % 60
converted.append(second)
dhms = ["일", "시간", "분", "초"]
result = []
for i in range(len(converted)):
  if converted[i] != 0:
    result.append(str(converted[i]) + dhms[i])
print(f"{time}초 = ", end = '')
for item in result:
  print(item, end = ' ')