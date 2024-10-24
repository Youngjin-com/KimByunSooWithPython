def is_bigger_than_max(max, target):
  if max < target:
    return True
  else:
    return False

lst = [10, 55, 66, 81, 10, 50, 78]
max_index = 0
for i in range(1, len(lst)):
  if is_bigger_than_max(lst[max_index], lst[i]):
    max_index = i
print(max_index)