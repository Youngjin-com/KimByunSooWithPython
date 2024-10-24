sec = int(input("시간(초)을 입력해 주세요. : ")) # 초 단위 시간 입력
print(str(sec) + "초 ", end='= ')
if sec >= 86400:
  temp = sec // 86400 
  sec -= temp * 86400
  print(str(temp) + '일', end=' ') 
if sec >= 3600:
  temp= sec // 3600 
  sec -= temp *3600 
  print(str(temp) + '시간', end=' ')
if sec >= 60:
  temp = sec // 60 
  sec -= temp * 60 
  print(str(temp) + '분', end=' ')
if sec != 0:
  print(str(sec) + '초')