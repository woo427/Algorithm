def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]
    stack = [0]
    
    for idx in range(1, len(prices)):
        while stack and prices[idx] < prices[stack[-1]]:
            value = stack.pop()
            answer[value] = idx - value
        stack.append(idx)
    return answer