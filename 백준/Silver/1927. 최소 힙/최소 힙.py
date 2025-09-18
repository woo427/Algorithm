import sys
import heapq

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
  num = int(sys.stdin.readline())
  if num == 0:
    if not nums:
      print(0)
    else:
      print(heapq.heappop(nums))
  else:
    heapq.heappush(nums, num)
