import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[v] = 1
list = []
list.append(v)

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n+1):
  graph[i].sort()

## dfs
def dfs(idx):
  for i in graph[idx]:
    if not visited[i]:
      list.append(i)
      visited[i] = 1
      dfs(i)
    # else:
    #   break


## bfs
q = deque()
q.append(v)
visited_b = [0] * (n+1)
visited_b[v] = 1
list_b = []

def bfs():
  while q:
    idx = q.popleft()
    list_b.append(idx)

    for j in graph[idx]:
      if not visited_b[j]:
        visited_b[j] = 1
        q.append(j)


## 출력
dfs(v)
print(' '.join(map(str, list)))

bfs()
print(' '.join(map(str, list_b)))
