def solution(num_list):
    answer = []
    length = len(num_list)
    for i in range(length - 1, -1, -1) :
        answer.append(num_list[i])
    return answer