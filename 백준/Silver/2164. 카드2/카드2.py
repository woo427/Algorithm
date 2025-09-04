import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()
count = 1

for i in range(1,n+1):
  q.append(i)

while len(q) != 1:
  if count % 2 != 0:
    q.popleft()
    count += 1
  else:
    num = q.popleft()
    q.append(num)
    count += 1

print(q.pop())
