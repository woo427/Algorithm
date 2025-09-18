import sys, math

t = int(sys.stdin.readline())

for _ in range(t):
  h, w, n = map(int, sys.stdin.readline().split())

  if n%h == 0:
    floor = h*100
  else:
    floor = (n%h)*100
  
  no = math.ceil(n/h)

  print(floor+no)