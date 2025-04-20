def solution(a, d, included):
    answer = 0
    
    for idx, is_included in enumerate(included):
        if is_included == True:
            answer += a + (d * idx)
    
    return answer