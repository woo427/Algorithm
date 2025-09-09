import sys

n = int(sys.stdin.readline())
str = sys.stdin.readline().strip()
count = 0
total = 0
m = 1234567891

for ch in str:
  num = ord(ch) - 96
  total += num * pow(31, count)
  count += 1

print(total % m)