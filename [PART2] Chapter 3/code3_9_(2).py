word = input()
if len(word) % 2 == 0:
  sel = int(len(word) / 2- 1)
  print(word[sel:sel + 2])
else:
  sel = int(len(word) / 2)
  print(word[sel])