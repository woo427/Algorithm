def solution(numbers):
    result = 0
    sum = 0
    for i in numbers:
        result += i
    for j in range(10):
        sum += j
    return sum - result