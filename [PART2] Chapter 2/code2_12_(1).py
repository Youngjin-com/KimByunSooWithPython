def is_prime(number):
  if number == 1:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

def get_prime_list(number):
  prime_numbers = []
  for num in range(2, number + 1):
    if is_prime(num):
      prime_numbers.append(num)
  return prime_numbers

num = int(input("숫자를 입력해 주세요. : "))
prime_numbers = get_prime_list(num)
for prime in prime_numbers:
  while True:
    if num % prime == 0:
      print(prime, end=" ")
      num /= prime
    else:
      break