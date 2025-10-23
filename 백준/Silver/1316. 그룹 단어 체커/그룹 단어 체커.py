import sys

n = int(sys.stdin.readline())
count = 0

for _ in range(n):
  s = sys.stdin.readline().strip()
  l = []

  for i in range(len(s)):
    if i == 0:
      l.append(s[0])
    else:
      if s[i] == s[i-1]:
        continue
      else:
        if s[i] not in l:
          l.append(s[i])
        else:
          break
  else:
    count += 1

print(count)
