import sys

T = int(sys.stdin.readline())

for _ in range(T):
  R, S = sys.stdin.readline().split()
  r = int(R)
  
  final = ""

  for ch in S:
    final += ch*r

  print(final)