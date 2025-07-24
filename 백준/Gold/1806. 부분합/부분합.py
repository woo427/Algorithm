import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

start = end = total = 0
length = N + 1

while True:
  if total >= S:
    length = min(length, (end - start))
    total -= nums[start]
    start += 1
  elif end == N:
    break
  else:
    total += nums[end]
    end += 1

print(length if length != N + 1 else 0)