import sys

s = sys.stdin.readline().strip()
cap_s = s.upper()
dic = {}

for ch in cap_s:
  if ch in dic:
    dic[ch] += 1
  else:
    dic[ch] = 1

val = max(dic.values())
result = []
for k, v in dic.items():
  if v == val:
    result.append(k)

if len(result) > 1:
  print('?')
else:
  print(result[0])