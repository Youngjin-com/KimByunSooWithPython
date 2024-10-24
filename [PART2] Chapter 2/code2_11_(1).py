while True:
  num = int(input("\n2부터 9 사이 숫자를 입력해 주세요. (1을 누르면 프로그램이 종료됩니다.) "))
  if num == 1: 
    print("프로그램을 종료합니다.")
    break

  if 2 <= num <= 9: 
    for i in range(1, 10): 
      print("%d * %d = %d"% (num, i, i * num))
  else:
      print("범위 외의 숫자입니다. 다시 시도하세요.")