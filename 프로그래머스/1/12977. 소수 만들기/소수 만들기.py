from itertools import combinations

def solution(nums):
    answer = 0
    
    com_list = list(combinations(nums,3))
    for num in com_list:
        if is_Prime(sum(num)):
            answer += 1
    return answer
    
def is_Prime(total):
    if total == 0 or total == 1:
        return False
    else:
        for i in range(2,(total//2)+1):
            if total % i == 0:
                return False
        return True