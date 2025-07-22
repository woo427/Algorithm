import sys

n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
   num = [int(sys.stdin.readline()) for _ in range(n)]
   num.sort()
   
   excl = int(n * 0.15 + 0.5)
   total = 0
   
   for i in range(excl, n-excl):
    total += num[i]
    
   print(int(total / (n-excl*2) + 0.5))