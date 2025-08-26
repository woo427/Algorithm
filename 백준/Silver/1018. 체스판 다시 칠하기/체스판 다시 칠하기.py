import sys

h, w = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(h)]
answer = []

for i in range(h-7):
  for j in range(w-7):
    color1 = 0
    color2 = 0

    for a in range(i, i+8):
      for b in range(j, j+8):

        if (a+b) % 2 == 0:
          if board[a][b] != 'B':
            color1 += 1
          if board[a][b] != 'W':
            color2 += 1
        else :
          if board[a][b] != 'B':
            color2 += 1
          if board[a][b] != 'W':
            color1 += 1
        
    answer.append(min(color1, color2))

print(min(answer))