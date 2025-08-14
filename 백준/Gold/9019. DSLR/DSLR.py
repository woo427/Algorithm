import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
  start, end = map(int, sys.stdin.readline().split())
  visited = [False] * 10000
  parent = [-1] * 10000
  how = [''] * 10000

  visited[start] = True
  q = deque([start])

  while q:
    num = q.popleft()

    if num == end:
      break

    for cmd, nxt in [
      ('D', (num*2)%10000),
      ('S', num-1 if num>0 else 9999),
      ('L', (num % 1000) * 10 + num // 1000),
      ('R', (num % 10) * 1000 + num // 10)
    ]:
      if not visited[nxt]:
        visited[nxt] = True
        parent[nxt] = num
        how[nxt] = cmd
        q.append(nxt)
  
  answer = []
  cur = end
  while cur != start:
    answer.append(how[cur])
    cur = parent[cur]
  
  print(''.join(reversed(answer)))