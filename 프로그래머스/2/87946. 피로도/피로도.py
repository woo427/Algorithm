import itertools

def solution(k, dungeons):
    case_list = list(itertools.permutations(dungeons))
    
    result = []
    for case in case_list:
        answer = 0
        total = k
        for i,j in case:
            if total < i:
                break
            else:
                total -= j
                answer += 1
        result.append(answer)
    return max(result)