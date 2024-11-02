def solution(absolutes, signs):
    answer = 0
    num = len(signs)
    for i in range(num):
        if signs[i] == True:
            answer += absolutes[i]
        else :
            answer -= absolutes[i]
    return answer