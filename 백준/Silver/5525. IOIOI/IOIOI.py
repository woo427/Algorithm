import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
S = sys.stdin.readline()

i = count = answer = 0

while i<(M-1):
  if S[i:i+3] == 'IOI':
    count += 1
    i += 2
    if count == N:
      count -= 1
      answer += 1
  else:
    count = 0
    i += 1

print(answer)