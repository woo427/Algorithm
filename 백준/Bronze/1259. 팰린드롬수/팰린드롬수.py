import sys

num = sys.stdin.readline().strip()
while num != '0':
  rever = ''
  for n in num:
    rever = n + rever

  if rever == num:
    print('yes')
  else:
    print('no')

  num = sys.stdin.readline().strip()