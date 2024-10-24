nums = [] 
for i in range(1, 6):
  n = int(input(f"{i}번째 숫자를 입력하세요 : "))
  nums.append(n) 

for i in range(5):
  for j in range(i, 5):
    if nums[i] > nums[j]:
      tmp = nums[i]
      nums[i] = nums[j]
      nums[j] = tmp
print("\n오름차순 :", nums)