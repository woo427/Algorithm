import itertools

def solution(numbers):
    box = []
    case = []
    answer = 0
    
    for i in range(1, len(numbers) + 1):
    	box += list(itertools.permutations(numbers, i))
    case = [int(''.join(b)) for b in box]
    
    for num in set(case):
        if isPrime(num):
            answer += 1
    return answer

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1) :
        if (num % i == 0):
            return False
    return True