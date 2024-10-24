print(
"""==========도형 목록==========
1. 원
2. 삼각형
3. 직사각형
4. 정사각형
============================""")
def circle() :
  r = int(input("원의 반지름 길이를 입력해 주세요. : "))
  print("반지름 길이가 %d인 원의 넓이는 약 %.2f입니다." % (r, round(3.14 *  r *  r, 2)))
def triangel() :
  h = int(input("삼각형 밑변의 길이를 입력해 주세요. : "))
  v = int(input("삼각형 높이의 길이를 입력해 주세요. : "))
  print("밑변이 %d이고 높이가 %d인 삼각형의 넓이는 %d입니다." % (h, v, h * v * 0.5))
def rectangle() :
  h = int(input("직사각형 가로 길이를 입력해 주세요. : "))
  v = int(input("직사각형 세로 길이를 입력해 주세요. : "))
  print("가로가 %d이고 세로가 %d인 직사각형의 넓이는 %d입니다." % (h, v, h * v))
def square() :
  n = int(input("정사각형 한 변의 길이를 입력해 주세요. : "))
  print("한 변이 %d인 정사각형의 넓이는 %d입니다." % (n, n * n))
num = int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해 주세요. : "))
if num == 1:
  circle()
elif num == 2:
  triangel()
elif num == 3:
  rectangle()
elif num == 4:
  square()