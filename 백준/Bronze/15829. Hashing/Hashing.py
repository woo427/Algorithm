import sys

n = int(sys.stdin.readline())
str = sys.stdin.readline().strip()
count = 0
total = 0

for ch in str:
  num = ord(ch) - 96
  total += num * pow(31, count)
  count += 1

print(total)