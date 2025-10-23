import sys

n = int(sys.stdin.readline())

for _ in range(n):
  s = sys.stdin.readline().strip()
  score = 0
  count = 0
  if s[0] == 'O':
    count = score = 1

  for idx in range(1, len(s)):
    if s[idx] == "O":
      if s[idx] == s[idx - 1]:
        count += 1
        score += count
      else:
        count = 1
        score += count
    else:
      count = 0
  
  print(score)
