num = [int(input()) for _ in range(10)]
list = []

for i in num:
  list.append(i % 42)
print(len(set(list)))