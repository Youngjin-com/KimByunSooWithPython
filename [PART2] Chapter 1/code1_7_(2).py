height = int(input("키를 입력하세요. : "))
weight = int(input("몸무게를 입력하세요. : "))
BMI = weight / (height * 0.01 * height * 0.01)
if BMI >= 25:
  print("BMI 지수가", BMI, "이므로 비만입니다.")
if 23 <= BMI < 25:
  print("BMI 지수가", BMI, "이므로 과체중입니다.")
if 18.5 <= BMI < 23:
  print("BMI 지수가", BMI, "이므로 정상체중입니다.")
if BMI < 18.5:
  print("BMI 지수가", BMI, "이므로 저체중입니다.")