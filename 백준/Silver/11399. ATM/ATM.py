import sys

N = int(sys.stdin.readline())
price = list(map(int, sys.stdin.readline().split()))
price.sort()

total = []
for i in range(len(price)):
  if i == 0:
    total.append(price[i])
  else:
    total.append(total[i-1] + price[i])

final = 0
for num in total:
  final += num

print(final)