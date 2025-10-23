import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
  arr.append(int(sys.stdin.readline().strip()))

arr.sort()

for num in arr:
  print(num)
