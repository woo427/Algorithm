import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

ladder = dict()
snake = dict()
for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  ladder[x] = y
for _ in range(n, n+m):
  x, y = map(int, sys.stdin.readline().split())
  snake[x] = y

visited = [False] * 101
board = [0] * 101

q = deque([1])
while q:
  x = q.popleft()
  if x == 100:
    print(board[x])
    break

  for dice in range(1,7):
    next = x + dice
    if next <= 100 and not visited[next]:
      if next in ladder.keys():
        next = ladder[next]
      if next in snake.keys():
        next = snake[next]
      if not visited[next]:
        visited[next] = True
        board[next] = board[x] + 1
        q.append(next)