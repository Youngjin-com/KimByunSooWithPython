class Point:
  def __init__(self, x, y): 
    self.x = x
    self.y = y
  def set_x(self, x):
    self.x = x
  def set_y(self, y):
    self.y = y
  def get(self): 
    return self.x, self.y
  def move(self, dx, dy):
    self.x += dx 
    self.y += dy 

x = int(input("x 좌표를 입력해 주세요. : "))
y = int(input("y 좌표를 입력해 주세요. : "))
a = Point(x, y) 
print("현재 좌표 :", a.get())
print("\nx 좌표 설정을 원한다면 x를, \ny 좌표 설정을 원한다면 y를, \n좌표 이동을 원한다면 m을, \n좌표 설정을 종료하려면 0을 입력해 주세요.")

while True:
  u = input("\n입력: ")
  if u == 'm':
    dx = int(input("x 좌표를 얼마만큼 이동할지 입력해 주세요. : "))
    dy = int(input("y 좌표를 얼마만큼 이동할지 입력해 주세요. : "))
    a.move(dx, dy)
  elif u == 'x':
    x = int(input("x 좌표를 입력해 주세요. : "))
    a.set_x(x)
  elif u == 'y':
    y = int(input("y 좌표를 입력해 주세요. : "))
    a.set_y(y)
  elif u == '0':
    break
  else: 
    print("잘못된 입력입니다.")
print("현재 좌표:", a.get())