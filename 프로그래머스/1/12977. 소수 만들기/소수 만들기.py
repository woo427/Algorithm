from itertools import combinations 

def solution(nums):
    answer = 0
    cmb_list = list(combinations(nums,3))
    for num_list in cmb_list:
        if is_prime(sum(num_list)):
            answer += 1
    return answer

def is_prime(sum):
    if sum == 0 or sum == 1:
        return False
    else :
        for i in range(2,(sum//2)+1):
            if sum % i == 0:
                return False
        return True
        