import sys

N = int(sys.stdin.readline())
data = {}

for _ in range(N):
  x,y = map(int,sys.stdin.readline().split())
  if x not in data:
    data[x] = []
  data[x].append(y)

s_data = sorted(data)
for num in s_data:
  if len(data[num]) > 1:
    val = sorted(data[num])
    for i in val:
      print(num, i)
  else:
    print(num, data[num][0])