import sys
import math

nums = list(map(int, sys.stdin.readline().split()))
total = 0

for num in nums:
  total += math.pow(num,2)

print(int(total % 10))