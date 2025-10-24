def solution(n):
    std = int(n ** 0.5)
    total = 0
    
    for i in range(1, std + 1):
        if n % i == 0:
            total += i
            if n // i != i:
                total += n // i
    return total