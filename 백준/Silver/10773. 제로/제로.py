import sys

k = int(sys.stdin.readline())
stack = []
total = 0

for _ in range(k):
  num = int(sys.stdin.readline())

  if num != 0:
    stack.append(num)
  else:
    stack.pop()

for i in stack:
  total += i

print(total)