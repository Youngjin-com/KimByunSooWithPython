class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def area(self):
    return self.width * self.height
  def round(self):
    return(self.width + self.height) * 2
w = int(input("가로: "))
h = int(input("세로: "))
a = Rectangle(w, h) # 클래스의 객체 a 생성
print("직사각형의 둘레는 %d이고, 넓이는 %d입니다." % (a.round(), a.area()))