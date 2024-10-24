class Calculator:
  def setdata(self, first, second):
    self.first = first
    self.second = second
  def result(self):
    result = self.second / 100
    pay = self.first * (1 - result)
    return pay
one = int(input("원가를 입력하세요. : "))
two = int(input("몇 퍼센트(%) 할인하나요? : "))
c = Calculator()
c.setdata(one, two)
print("최종 금액은", c.result(), "입니다.")