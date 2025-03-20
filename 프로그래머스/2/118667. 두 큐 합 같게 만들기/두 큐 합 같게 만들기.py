from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    total = sum_q1 + sum_q2
    answer = 0
    
    if total % 2 != 0:
        return -1
    
    target = total // 2
    max = 3 * len(q1)
    
    while sum_q1 != sum_q2:
        if answer > max:
            return -1
        
        if sum_q1 < sum_q2:
            value = q2.popleft()
            q1.append(value)
            sum_q1 += value
            sum_q2 -= value
            
        elif sum_q1 > sum_q2:
            value = q1.popleft()
            q2.append(value)
            sum_q1 -= value
            sum_q2 += value
            
        answer += 1
    return answer