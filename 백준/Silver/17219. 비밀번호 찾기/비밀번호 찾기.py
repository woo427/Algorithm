import sys

n, m = map(int, sys.stdin.readline().split())
address = {}
address = dict()
answer = []

for _ in range(n):
  url, pwd = sys.stdin.readline().split()
  address[url] = pwd

for _ in range(m):
  search_url = sys.stdin.readline().strip()
  if search_url in address.keys():
    print(address[search_url])