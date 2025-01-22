def solution(money):
    answer = []
    i = 1
    while(1) :
        if money - 5500*i < 0 :
            total = money - 5500*(i-1)
            answer.append(i - 1)
            answer.append(total)
            break
        i += 1
    return answer