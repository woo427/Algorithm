import sys

n = int(sys.stdin.readline())

for _ in range(n):
  num, *scores = map(int, sys.stdin.readline().split())
  avg = sum(scores) / num
  count = 0

  for score in scores:
    if score > avg:
      count += 1

  print(f"{(count / num) * 100:.3f}%")
