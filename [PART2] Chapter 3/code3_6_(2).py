def num_reverse(n): 
  rev_n = int(n[::-1])
  return rev_n
def num_prime(n): # 소수 판별 함수
  if n < 2: 
    return False  
  for p in range(2, n):
    if n % p == 0:  
      return False 
  return True 

print('< \'뒤집은 소수\'판별 프로그램 >\n')
count = int(input('입력받을 숫자의 개수를 입력해 주세요. : '))
prime_dict = {} 
for i in range(1, count + 1):
  num = input(f'각 {i}번째 숫자를 입력해주세요 : ') 
  rev_num = num_reverse(num) 
  if num_prime(rev_num):    
    prime_dict[i] = num  
print()
print('*' * 11, '판별 결과', '*' * 11)
if len(prime_dict) == 0:
  print('뒤집은 소수는 존재하지 않습니다.')
else:
  key_list= list(prime_dict.keys())
  for k in key_list:
    kth_num= prime_dict[k]
    kth_rev= num_reverse(kth_num)
    print(f'{k}번째로 입력하신 숫자는 뒤집은 소수입니다. ({kth_num} -> {kth_rev})') 