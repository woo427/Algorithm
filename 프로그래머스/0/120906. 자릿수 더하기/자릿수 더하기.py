def solution(n):
    answer = 0
    n_str = str(n)
    for num in n_str:
        answer += int(num)
    return answer