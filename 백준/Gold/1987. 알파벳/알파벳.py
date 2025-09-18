import sys

r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]

visited = [0] * 26
visited[ord(board[0][0]) - ord('A')] = 1
count = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x,y,depth):
  global count
  count = max(count, depth)
  

  for i in range(4):
    next_x = x + dx[i]
    next_y = y + dy[i]

    if 0<=next_x<r and 0<=next_y<c and visited[ord(board[next_x][next_y]) - ord('A')] == 0:
      visited[ord(board[next_x][next_y]) - ord('A')] = 1
      dfs(next_x, next_y, depth+1)
      visited[ord(board[next_x][next_y]) - ord('A')] = 0

dfs(0,0,1)
print(count)