import sys

n = int(sys.stdin.readline())
data = []

for idx in range(1,n+1):
  age, name = sys.stdin.readline().split()
  data.append([idx, int(age), name])

data.sort(key= lambda x: (x[1], x[0]))

for d in data:
  print(d[1], d[2])