import sys

nums = [int(line.strip()) for line in sys.stdin.readlines()]

max_num = max(nums)
max_idx = nums.index(max_num)

print(max_num)
print(max_idx + 1)