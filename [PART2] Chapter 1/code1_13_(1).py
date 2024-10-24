class Calculator:
  def __init__(self, price, discount):
    self.price = price
    self.discount = discount
  def getResult(self):
    return self.price - (self.price * self.discount / 100)
price = int(input("원가를 입력하세요. : "))
discount = int(input("몇 퍼센트(%) 할인하나요? : "))
calculator = Calculator(price, discount)
print("최종 금액은", calculator.getResult(), "입니다.")