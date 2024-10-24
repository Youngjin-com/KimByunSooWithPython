word = input()
mid_word = ''
if len(word) % 2 == 0:
  num = len(word) // 2 
  mid_word += word[num - 1] + word[num] 
else: 
  num = len(word) // 2 
  mid_word += word[num]
print(mid_word)