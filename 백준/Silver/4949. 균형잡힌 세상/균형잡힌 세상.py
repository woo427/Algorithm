import sys

while True:
  stack = []
  sentence = sys.stdin.readline().rstrip()

  if sentence == '.':
    break

  for ch in sentence:
    if ch == '(':
      stack.append(')')
    elif ch == '[':
      stack.append(']')
    elif ch == ')' or ch == ']':
      if stack:
        st = stack.pop()
        if st != ch:
          print('no')
          break
      else:
        print('no')
        break

  else:
    if not stack:
      print('yes')
    else:
      print('no')