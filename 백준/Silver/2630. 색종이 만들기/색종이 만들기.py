import sys

n = int(sys.stdin.readline())

map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = []


def solution(x,y,size):
  color = map[x][y]

  for i in range(x, x+size):
    for j in range(y, y+size):
      if color != map[i][j]:
        solution(x,y,size//2)
        solution(x,y+size//2,size//2)
        solution(x+size//2,y,size//2)
        solution(x+size//2,y+size//2,size//2)
        return
  
  if color == 0:
    result.append(0)
  else:
    result.append(1)


solution(0,0,n)
print(result.count(0))
print(result.count(1))